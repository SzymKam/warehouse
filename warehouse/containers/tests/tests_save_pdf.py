import secrets

from django.test import TestCase, Client, tag
from django.urls import reverse
from rest_framework import status
from faker import Faker

from staff.models import StaffModel
from containers.models import Container

DETAIL_URL = "save-pdf"


class SavePdfTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.fake = Faker()

        self.user_1 = StaffModel.objects.create(
            username=self.fake.name(), password=secrets.token_hex(nbytes=8)
        )

        self.container_1 = Container.objects.create(name="Main warehouse")

    @staticmethod
    def detail_url(element):
        return reverse(
            DETAIL_URL, kwargs={"element": "containers", "element_id": element.pk}
        )

    @tag("test")
    def test_get_not_logged_user_return_302(self):
        response = self.client.get(path=self.detail_url(self.container_1))

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")

    @tag("test")
    def test_get_logged_user_return_200(self):
        self.client.force_login(self.user_1)
        response = self.client.get(path=self.detail_url(self.container_1))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")

    @tag("test")
    def test_post_not_logged_user_return_302(self):
        response = self.client.post(path=self.detail_url(self.container_1))

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

    @tag("test")
    def test_post_logged_user_return_200(self):
        self.client.force_login(self.user_1)
        response = self.client.post(path=self.detail_url(self.container_1))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

    @tag("test")
    def test_patch_not_logged_user_return_302(self):
        response = self.client.patch(path=self.detail_url(self.container_1))

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")

    @tag("test")
    def test_patch_logged_user_return_200(self):
        self.client.force_login(self.user_1)
        response = self.client.patch(path=self.detail_url(self.container_1))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")

    @tag("test")
    def test_delete_not_logged_user_return_302(self):
        response = self.client.delete(path=self.detail_url(self.container_1))

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")

    @tag("test")
    def test_delete_logged_user_return_200(self):
        self.client.force_login(self.user_1)
        response = self.client.delete(path=self.detail_url(self.container_1))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")
