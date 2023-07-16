import secrets
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from faker import Faker

from staff.models import StaffModel


DETAIL_URL = "main-page"


class MainPageTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.fake = Faker()

        self.user_1 = StaffModel.objects.create(
            username=self.fake.name(), password=secrets.token_hex(nbytes=8)
        )

    def test_get_not_logged_user_return_302(self) -> None:
        response = self.client.get(path=reverse(DETAIL_URL))

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")

    def test_get_logged_user_return_200(self) -> None:
        self.client.force_login(self.user_1)

        response = self.client.get(path=reverse(DETAIL_URL))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")
        self.assertTemplateUsed("containers/main-page.html")

    def test_post_not_logged_user_return_302(self) -> None:
        response = self.client.post(path=reverse(DETAIL_URL))

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

    def test_post_logged_user_return_405(self) -> None:
        self.client.force_login(self.user_1)
        response = self.client.post(path=reverse(DETAIL_URL))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

    def test_patch_not_logged_user_return_302(self) -> None:
        response = self.client.patch(path=reverse(DETAIL_URL))

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")

    def test_patch_logged_user_return_405(self) -> None:
        self.client.force_login(self.user_1)
        response = self.client.patch(path=reverse(DETAIL_URL))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")

    def test_delete_not_logged_user_return_302(self) -> None:
        response = self.client.delete(path=reverse(DETAIL_URL))

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")

    def test_delete_logged_user_return_405(self) -> None:
        self.client.force_login(self.user_1)
        response = self.client.delete(path=reverse(DETAIL_URL))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")
