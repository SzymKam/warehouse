import secrets

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import Permission
from rest_framework import status
from faker import Faker

from staff.models import StaffModel


DETAIL_URL = "register"


class StaffRegisterTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.fake = Faker()

        self.user_1 = StaffModel.objects.create(
            username=self.fake.name(), password=secrets.token_hex(nbytes=8)
        )
        self.user_2 = StaffModel.objects.create(
            username=self.fake.name(), password=secrets.token_hex(nbytes=8)
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

    def test_get_not_logged_return_302(self) -> None:
        response = self.client.get(path=reverse(DETAIL_URL))

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")

    def test_get_logged_user_no_permissions_return_302(self) -> None:
        self.client.force_login(self.user_2)

        response = self.client.get(path=reverse(DETAIL_URL))

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")

    def test_get_logged_user_have_permissions_return_200(self) -> None:
        self.client.force_login(self.user_1)

        response = self.client.get(path=reverse(DETAIL_URL))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")
        self.assertEqual(response.context["title"], "GRM Register")
        self.assertTemplateUsed("staff/register.html")

    def test_delete_not_logged_return_302(self) -> None:
        response = self.client.delete(path=reverse(DETAIL_URL))

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")

    def test_delete_logged_user_no_permissions_return_302(self) -> None:
        self.client.force_login(self.user_2)

        response = self.client.delete(path=reverse(DETAIL_URL))

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")

    def test_delete_logged_user_have_permissions_return_200(self) -> None:
        self.client.force_login(self.user_1)

        response = self.client.delete(path=reverse(DETAIL_URL))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")
        self.assertEqual(response.context["title"], "GRM Register")
        self.assertTemplateUsed("staff/register.html")

    def test_patch_not_logged_return_302(self) -> None:
        response = self.client.patch(path=reverse(DETAIL_URL))

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")

    def test_patch_logged_user_no_permissions_return_302(self) -> None:
        self.client.force_login(self.user_2)

        response = self.client.patch(path=reverse(DETAIL_URL))

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")

    def test_patch_logged_user_have_permissions_return_200(self) -> None:
        self.client.force_login(self.user_1)

        response = self.client.patch(path=reverse(DETAIL_URL))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")
        self.assertEqual(response.context["title"], "GRM Register")
        self.assertTemplateUsed("staff/register.html")

    def test_post_not_logged_return_302(self) -> None:
        response = self.client.post(path=reverse(DETAIL_URL))

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

    def test_post_logged_user_no_permissions_return_302(self) -> None:
        self.client.force_login(self.user_2)

        response = self.client.post(path=reverse(DETAIL_URL))

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

    def test_post_logged_user_have_permissions_return_200(self) -> None:
        self.client.force_login(self.user_1)

        response = self.client.post(path=reverse(DETAIL_URL))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")
        self.assertEqual(response.context["title"], "GRM Register")
        self.assertTemplateUsed("staff/register.html")
