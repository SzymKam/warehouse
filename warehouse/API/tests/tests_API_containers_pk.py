import secrets

from django.contrib.auth.models import Permission
from django.test import TestCase, tag
from containers.models import Drug, Container
from staff.models import StaffModel
from django.urls import reverse
from rest_framework import status
from warehouse.env import env


class TestContainersResponse(TestCase):
    def setUp(self) -> None:
        self.user = StaffModel.objects.create(
            username="nimda", password=secrets.token_hex(nbytes=10)
        )
        self.container_1 = Container.objects.create(name="Main warehouse")
        self.container_2 = Container.objects.create(
            name="Special/Other", description="container_2"
        )

    def test_get_not_logged_user_return_403(self):
        url = reverse("container-detail", kwargs={"pk": 1})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")

    def test_get_logged_user_no_permissions_return_right_value(self):
        object_to_get = Container.objects.filter(name=self.container_1.name).first()
        url = reverse("container-detail", kwargs={"pk": object_to_get.id})

        self.client.force_login(self.user)

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")
        self.assertEqual(response.data["name"], self.container_1.name)
        self.assertEqual(response.data["id"], self.container_1.id)
        self.assertEqual(response.data["description"], self.container_1.description)

    def test_post_logged_have_permissions_user_container_name_in_list_create_container(
        self,
    ):
        url = reverse("container-detail", kwargs={"pk": 99})

        self.client.force_login(self.user)
        self.permission = Permission.objects.get(codename="add_container")
        self.user.user_permissions.add(self.permission)

        data = {"name": "Backpack - R1", "description": "test_r1"}
        response = self.client.post(path=url, data=data)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

    def test_post_logged_have_permissions_user_container_name_not_in_list_return_405(
        self,
    ):
        url = reverse("container-detail", kwargs={"pk": 99})

        self.client.force_login(self.user)
        self.permission = Permission.objects.get(codename="add_container")
        self.user.user_permissions.add(self.permission)

        data = {"name": "some_name", "description": "test_r1"}
        response = self.client.post(path=url, data=data)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

    def test_post_logged_no_permissions_user_container_name_in_list_create_container(
        self,
    ):
        url = reverse("container-detail", kwargs={"pk": 99})

        self.client.force_login(self.user)

        data = {"name": "Backpack - R1", "description": "test_r1"}
        response = self.client.post(path=url, data=data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

    def test_post_not_logged_user_return_403(self):
        url = reverse("container-detail", kwargs={"pk": 99})

        data = {"name": "Backpack - R1", "description": "test_r1"}
        response = self.client.post(path=url, data=data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

    def test_patch_logged_user_have_permissions_id_in_list_return_200(self):
        object_to_patch = Container.objects.filter(name=self.container_2.name).first()
        url = reverse("container-detail", kwargs={"pk": object_to_patch.id})

        self.client.force_login(self.user)
        self.permission = Permission.objects.get(codename="change_container")
        self.user.user_permissions.add(self.permission)

        data = {"description": "updated_container_2"}
        response = self.client.patch(
            path=url, data=data, content_type="application/json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")
        self.assertEqual(response.data["name"], object_to_patch.name)
        self.assertEqual(response.data["description"], data["description"])

    def test_patch_logged_user_have_permissions_id_not_in_list_return_404(self):
        url = reverse("container-detail", kwargs={"pk": 9999})

        self.client.force_login(self.user)
        self.permission = Permission.objects.get(codename="change_container")
        self.user.user_permissions.add(self.permission)

        data = {"description": "updated_container_2"}
        response = self.client.patch(
            path=url, data=data, content_type="application/json"
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")

    def test_patch_logged_user_no_permissions_id_in_list_return_403(self):
        object_to_patch = Container.objects.filter(name=self.container_2.name).first()
        url = reverse("container-detail", kwargs={"pk": object_to_patch.id})

        self.client.force_login(self.user)

        data = {"description": "updated_container_2"}
        response = self.client.patch(
            path=url, data=data, content_type="application/json"
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")

    def test_patch_not_logged_user_id_in_list_return_403(self):
        object_to_patch = Container.objects.filter(name=self.container_2.name).first()
        url = reverse("container-detail", kwargs={"pk": object_to_patch.id})

        data = {"description": "updated_container_2"}
        response = self.client.patch(
            path=url, data=data, content_type="application/json"
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")

    def test_delete_logged_user_have_permissions_id_in_list_return_204(self):
        object_to_delete = Container.objects.filter(name=self.container_2.name).first()
        url = reverse("container-detail", kwargs={"pk": object_to_delete.id})

        self.client.force_login(self.user)
        self.permission = Permission.objects.get(codename="delete_container")
        self.user.user_permissions.add(self.permission)

        response = self.client.delete(path=url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")

    def test_delete_logged_user_have_permissions_id_not_in_list_return_404(self):
        url = reverse("container-detail", kwargs={"pk": 99999})

        self.client.force_login(self.user)
        self.permission = Permission.objects.get(codename="delete_container")
        self.user.user_permissions.add(self.permission)

        response = self.client.delete(path=url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")

    def test_delete_logged_user_no_permissions_id_in_list_return_403(self):
        object_to_delete = Container.objects.filter(name=self.container_2.name).first()
        url = reverse("container-detail", kwargs={"pk": object_to_delete.id})

        self.client.force_login(self.user)

        response = self.client.delete(path=url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")

    def test_delete_not_logged_user_return_403(self):
        object_to_delete = Container.objects.filter(name=self.container_2.name).first()
        url = reverse("container-detail", kwargs={"pk": object_to_delete.id})

        response = self.client.delete(path=url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")
