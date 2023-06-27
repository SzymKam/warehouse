from django.test import TestCase, Client, tag
from django.urls import reverse
from django.contrib.auth.models import Permission
from rest_framework import status

from staff.models import StaffModel
from warehouse import env


DETAIL_URL = "delete-user"


class StaffDeleteTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()

        self.user_1 = StaffModel.objects.create(
            username="nimda", password=env("TEST_PASSWORD")
        )
        self.user_2 = StaffModel.objects.create(
            username="test_2", password=env("TEST_PASSWORD")
        )
        self.user_3 = StaffModel.objects.create(
            username="test_3", password=env("TEST_PASSWORD")
        )

        self.template_used = "staff/delete.html"

    def detail_url(self, obj):
        return reverse(DETAIL_URL, kwargs={"pk": obj.pk})

    def test_get_not_logged_user_return_302(self):
        url = self.detail_url(self.user_3)
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")
        self.assertTemplateUsed(response, self.template_used)

    def test_get_logged_user_return_302(self):
        self.client.force_login(self.user_1)

        response = self.client.get(self.detail_url(self.user_3))

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")
        self.assertTemplateUsed(response, self.template_used)

    @tag("test")
    def test_get_logged_user_have_permissions_return_302(self):
        self.client.force_login(self.user_1)
        self.permission = Permission.objects.get(codename="delete_staffmodel")
        self.user_1.user_permissions.add(self.permission)

        response = self.client.get(self.detail_url(self.user_3))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")
        self.assertTemplateUsed(response, self.template_used)
