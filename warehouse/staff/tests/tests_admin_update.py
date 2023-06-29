import secrets

from django.test import TestCase, Client, tag
from django.urls import reverse
from django.contrib.auth.models import Permission
from rest_framework import status

from staff.models import StaffModel


DETAIL_URL = "admin-update"


class StaffDeleteTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()

        self.user_1 = StaffModel.objects.create(
            username="admin", password=secrets.token_hex(nbytes=8)
        )
        self.user_2 = StaffModel.objects.create(
            username="test_2", password=secrets.token_hex(nbytes=8)
        )
        self.user_3 = StaffModel.objects.create(
            username="test_3", password=secrets.token_hex(nbytes=8)
        )

        self.template_used = "staff/delete.html"

        self.user_1.user_permissions.add(
            Permission.objects.get(codename="add_staffmodel")
        )
        self.user_1.user_permissions.add(
            Permission.objects.get(codename="change_staffmodel")
        )
        self.user_1.user_permissions.add(
            Permission.objects.get(codename="delete_staffmodel")
        )

    @staticmethod
    def detail_url(obj):
        return reverse(DETAIL_URL, kwargs={"pk": obj.pk})

    def test_get_not_logged_user_return_302(self):
        response = self.client.get(path=self.detail_url(self.user_2))

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")

    # @tag('test')
    # def test_get_logged_user_return_(self):
    #     self.client.force_login(self.user_3)
    #
    #     response = self.client.get(path=self.detail_url(self.user_2))
    #
    #     self.assertEqual(response.status_code, status.HTTP_302_FOUND)
    #     self.assertEqual(response.request["REQUEST_METHOD"], "GET")
