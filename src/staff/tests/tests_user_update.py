import secrets

from django.test import TestCase, Client, tag
from django.urls import reverse
from rest_framework import status
from faker import Faker

from staff.models import StaffModel


DETAIL_URL = "update"


class StaffUpdateByUserTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.fake = Faker()

        self.user_1 = StaffModel.objects.create(
            username=self.fake.name(), password=secrets.token_hex(nbytes=8)
        )
        self.user_2 = StaffModel.objects.create(
            username=self.fake.name(), password=secrets.token_hex(nbytes=8)
        )
        self.user_3 = StaffModel.objects.create(
            username=self.fake.name(), password=secrets.token_hex(nbytes=8)
        )

        self.template_used = "staff/delete.html"

    @staticmethod
    def detail_url(obj):
        return reverse(DETAIL_URL, kwargs={"pk": obj.pk})

    def test_get_not_logged_user_return_302(self):
        response = self.client.get(path=self.detail_url(self.user_2))

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")

    def test_get_logged_user_return_200(self):
        self.client.force_login(self.user_2)

        response = self.client.get(path=self.detail_url(self.user_2))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")

    def test_post_not_logged_user_return_302(self):
        response = self.client.post(path=self.detail_url(self.user_2))

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

    def test_post_logged_user_return_200(self):
        self.client.force_login(self.user_2)

        response = self.client.post(path=self.detail_url(self.user_2))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

    def test_patch_logged_user_return_200(self):
        self.client.force_login(self.user_3)
        response = self.client.patch(path=self.detail_url(self.user_2))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")

    def test_patch_not_logged_user_return_302(self):
        response = self.client.patch(path=self.detail_url(self.user_2))

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")

    def test_delete_not_logged_user_return_302(self):
        response = self.client.delete(path=self.detail_url(self.user_2))

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")

    def test_delete_logged_user_return_302(self):
        self.client.force_login(self.user_3)
        response = self.client.delete(path=self.detail_url(self.user_2))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")
