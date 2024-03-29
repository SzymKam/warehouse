import secrets

from django.contrib.auth.models import Permission
from django.test import TestCase
from staff.models import StaffModel
from django.urls import reverse
from rest_framework import status


class TestStaffResponse(TestCase):
    def setUp(self) -> None:
        self.user_1 = StaffModel.objects.create(
            username="nimda", password=secrets.token_hex(nbytes=10)
        )
        self.user_2 = StaffModel.objects.create(
            username="test_2", password=secrets.token_hex(nbytes=10)
        )
        self.user_3 = StaffModel.objects.create(
            username="test_3", password=secrets.token_hex(nbytes=10)
        )

    def test_get_logged_user_return_right_values_with_two_objects(self):
        url = reverse("staffmodel-list")
        self.client.force_login(self.user_1)
        response = self.client.get(url)

        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")

    def test_get_not_logged_user_return_403(self):
        url = reverse("staffmodel-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")

    def test_post_logged_have_permissions_user_return_201(self):
        url = reverse("staffmodel-list")
        self.client.force_login(self.user_1)
        self.permission = Permission.objects.get(codename="add_staffmodel")
        self.user_1.user_permissions.add(self.permission)

        data = {"username": "test_4", "password": secrets.token_hex(nbytes=8)}
        response = self.client.post(path=url, data=data)

        self.assertEqual(response.request["REQUEST_METHOD"], "POST")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["username"], data["username"])
        self.assertEqual(response.data["password"], data["password"])

    def test_post_logged_user_no_permissions_return_403(self):
        url = reverse("staffmodel-list")
        self.client.force_login(self.user_1)

        response = self.client.post(path=url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

    def test_post_not_logged_user_return_403(self):
        url = reverse("staffmodel-list")

        response = self.client.post(path=url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

    def test_patch_logged_have_permissions_user_return_405(self):
        url = reverse("staffmodel-list")

        self.client.force_login(self.user_1)
        self.permission = Permission.objects.get(codename="change_staffmodel")
        self.user_1.user_permissions.add(self.permission)

        response = self.client.patch(path=url)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")

    def test_patch_logged_user_no_permissions_return_403(self):
        url = reverse("staffmodel-list")
        self.client.force_login(self.user_1)

        response = self.client.patch(path=url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")

    def test_patch_not_logged_user_return_403(self):
        url = reverse("staffmodel-list")
        response = self.client.patch(path=url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")

    def test_delete_logged_have_permissions_user_return_405(self):
        url = reverse("staffmodel-list")

        self.client.force_login(self.user_1)
        self.permission = Permission.objects.get(codename="delete_staffmodel")
        self.user_1.user_permissions.add(self.permission)

        response = self.client.delete(path=url)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")

    def test_delete_logged_user_no_permissions_return_403(self):
        url = reverse("staffmodel-list")
        self.client.force_login(self.user_1)

        response = self.client.delete(path=url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")

    def test_delete_not_logged_user_return_403(self):
        url = reverse("staffmodel-list")
        response = self.client.delete(path=url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")
