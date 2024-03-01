import secrets

from django.contrib.auth.models import Permission
from django.test import TestCase
from containers.models import Container
from staff.models import StaffModel
from django.urls import reverse
from rest_framework import status


class TestContainersResponse(TestCase):
    def setUp(self) -> None:
        self.user = StaffModel.objects.create(
            username="nimda", password=secrets.token_hex(nbytes=10)
        )
        self.container_1 = Container.objects.create(name="Warehouse")
        self.container_2 = Container.objects.create(name="Special/Other")

    def test_get_not_logged_user_return_403(self):
        url = reverse("container-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")

    def test_get_logged_user_no_permissions_return_right_value(self):
        url = reverse("container-list")
        self.client.force_login(self.user)

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0]["name"], "Main warehouse")
        self.assertEqual(response.data[1]["name"], self.container_1.name)
        self.assertEqual(response.data[2]["name"], self.container_2.name)
        self.assertEqual(response.data[1]["id"], self.container_1.id)
        self.assertEqual(response.data[2]["id"], self.container_2.id)
        self.assertEqual(response.data[1]["description"], self.container_1.description)
        self.assertEqual(response.data[2]["description"], self.container_2.description)

    def test_post_logged_have_permissions_user_container_name_in_list_create_container(
        self,
    ):
        url = reverse("container-list")

        self.client.force_login(self.user)
        self.permission = Permission.objects.get(codename="add_container")
        self.user.user_permissions.add(self.permission)

        data = {"name": "Backpack - R1", "description": "test_r1"}
        response = self.client.post(path=url, data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")
        self.assertEqual(response.data["name"], data["name"])
        self.assertEqual(response.data["description"], data["description"])

    def test_post_logged_have_permissions_user_container_name_not_in_list_return_400(
        self,
    ):
        url = reverse("container-list")

        self.client.force_login(self.user)
        self.permission = Permission.objects.get(codename="add_container")
        self.user.user_permissions.add(self.permission)

        data = {"name": "some name", "description": "test_r1"}
        response = self.client.post(path=url, data=data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

    def test_post_logged_user_no_permission_return_403(self):
        url = reverse("container-list")

        self.client.force_login(self.user)

        data = {"name": "Backpack - R1", "description": "test_r1"}
        response = self.client.post(path=url, data=data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

    def test_post_not_logged_user_return_403(self):
        url = reverse("container-list")

        data = {"name": "Backpack - R1", "description": "test_r1"}
        response = self.client.post(path=url, data=data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

    def test_patch_not_logged_user_return_403(self):
        url = reverse("container-list")

        response = self.client.patch(path=url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")

    def test_patch_logged_user_no_permissions_return_403(self):
        url = reverse("container-list")
        self.client.force_login(self.user)
        response = self.client.patch(path=url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")

    def test_patch_logged_user_have_permissions_return_405(self):
        url = reverse("container-list")
        self.client.force_login(self.user)
        self.permission = Permission.objects.get(codename="change_container")
        self.user.user_permissions.add(self.permission)

        response = self.client.patch(path=url)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")

    def test_delete_not_logged_user_return_403(self):
        url = reverse("container-list")

        response = self.client.delete(path=url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")

    def test_delete_logged_user_no_permissions_return_403(self):
        url = reverse("container-list")
        self.client.force_login(self.user)
        response = self.client.delete(path=url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")

    def test_delete_logged_user_have_permissions_return_405(self):
        url = reverse("container-list")
        self.client.force_login(self.user)
        self.permission = Permission.objects.get(codename="delete_container")
        self.user.user_permissions.add(self.permission)

        response = self.client.delete(path=url)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")
