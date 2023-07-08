import secrets

from django.test import TestCase, Client, tag
from django.urls import reverse
from django.contrib.auth.models import Permission
from rest_framework import status

from staff.models import StaffModel


DETAIL_URL = "delete-user"


class StaffDeleteTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()

        self.user_1 = StaffModel.objects.create(
            username="nimda", password=secrets.token_hex(nbytes=8)
        )
        self.user_2 = StaffModel.objects.create(
            username="test_2", password=secrets.token_hex(nbytes=8)
        )
        self.user_3 = StaffModel.objects.create(
            username="test_3", password=secrets.token_hex(nbytes=8)
        )

        self.template_used = "staff/delete.html"

        self.user_2.user_permissions.add(
            Permission.objects.get(codename="add_staffmodel")
        )
        self.user_2.user_permissions.add(
            Permission.objects.get(codename="change_staffmodel")
        )
        self.user_2.user_permissions.add(
            Permission.objects.get(codename="delete_staffmodel")
        )

    @staticmethod
    def detail_url(obj):
        return reverse(DETAIL_URL, kwargs={"pk": obj.pk})

    def test_get_not_logged_user_return_302(self):
        url = self.detail_url(self.user_3)
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")

    def test_get_logged_user_return_302(self):
        self.client.force_login(self.user_1)

        response = self.client.get(self.detail_url(self.user_3))

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")

    def test_post_logged_user_return_302(self):
        self.client.force_login(self.user_1)

        response = self.client.post(self.detail_url(self.user_3))

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

    def test_post_not_logged_user_return_302(self):
        response = self.client.post(self.detail_url(self.user_3))

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

    def test_patch_logged_user_return_302(self):
        self.client.force_login(self.user_1)

        response = self.client.patch(self.detail_url(self.user_3))

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")

    def test_patch_not_logged_user_return_302(self):
        response = self.client.patch(self.detail_url(self.user_3))

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")

    def test_delete_not_logged_user_return_302(self):
        response = self.client.delete(self.detail_url(self.user_3))

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")

    def test_delete_logged_user_return_302(self):
        self.client.force_login(self.user_1)

        response = self.client.delete(self.detail_url(self.user_3))

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")

    def test_get_logged_user_have_permissions_return_200(self):
        self.client.force_login(self.user_2)

        response = self.client.get(self.detail_url(self.user_3))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")

    def test_delete_logged_user_have_permissions_return_200(self):
        self.client.force_login(self.user_2)

        response = self.client.delete(self.detail_url(self.user_3))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")

    def test_patch_logged_user_have_permissions_return_200(self):
        self.client.force_login(self.user_2)

        response = self.client.patch(self.detail_url(self.user_3))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")

    def test_post_logged_user_have_permissions_return_(self):
        self.client.force_login(self.user_2)

        response = self.client.post(self.detail_url(self.user_3))

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")
