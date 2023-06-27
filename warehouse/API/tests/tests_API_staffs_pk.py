from django.contrib.auth.models import Permission
from django.test import TestCase, tag
from containers.models import OxygenMask, Container
from staff.models import StaffModel
from django.urls import reverse
from rest_framework import status
from warehouse.env import env


class TestStaffResponse(TestCase):
    def setUp(self) -> None:
        self.user_1 = StaffModel.objects.create(
            username="nimda", password=env("TEST_PASSWORD")
        )
        self.user_2 = StaffModel.objects.create(
            username="test_2", password=env("TEST_PASSWORD")
        )
        self.user_3 = StaffModel.objects.create(
            username="test_3", password=env("TEST_PASSWORD")
        )

    def test_get_not_logged_user_return_403(self):
        url = reverse("staffmodel-detail", kwargs={"pk": 1})

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")

    def test_get_logged_user_return_right_values_from_object(self):
        object_to_get = StaffModel.objects.filter(username="test_2").first()
        url = reverse("staffmodel-detail", kwargs={"pk": object_to_get.id})

        self.client.force_login(self.user_1)

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")
        self.assertEqual(response.data["id"], object_to_get.id)
        self.assertEqual(response.data["username"], object_to_get.username)

    def test_get_logged_user_return_404_when_object_not_exist(self):
        url = reverse("staffmodel-detail", kwargs={"pk": 100000})

        self.client.force_login(self.user_1)

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")

    def test_post_logged_have_permissions_user_return_405(self):
        url = reverse("staffmodel-detail", kwargs={"pk": 1})

        self.client.force_login(self.user_1)
        self.permission = Permission.objects.get(codename="add_staffmodel")
        self.user_1.user_permissions.add(self.permission)

        response = self.client.post(path=url)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

    def test_post_logged_user_no_permissions_return_403(self):
        url = reverse("staffmodel-detail", kwargs={"pk": 1})

        self.client.force_login(self.user_1)

        response = self.client.post(path=url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

    def test_post_not_logged_user_return_403(self):
        url = reverse("staffmodel-detail", kwargs={"pk": 1})

        response = self.client.post(path=url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

    def test_patch_logged_have_permissions_user_return_right_value(self):
        object_to_patch = StaffModel.objects.filter(username="test_2").first()
        url = reverse("staffmodel-detail", kwargs={"pk": object_to_patch.id})

        self.client.force_login(self.user_1)
        self.permission = Permission.objects.get(codename="change_staffmodel")
        self.user_1.user_permissions.add(self.permission)

        data = {"username": "changed_username"}
        response = self.client.patch(
            path=url, data=data, content_type="application/json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")
        self.assertEqual(response.data["id"], object_to_patch.id)
        self.assertEqual(response.data["username"], data["username"])

    def test_patch_logged_have_permissions_user_object_not_exist_return_404(self):
        url = reverse("staffmodel-detail", kwargs={"pk": 99999})

        self.client.force_login(self.user_1)
        self.permission = Permission.objects.get(codename="change_staffmodel")
        self.user_1.user_permissions.add(self.permission)

        response = self.client.patch(path=url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")

    def test_patch_logged_user_no_permissions_return_403(self):
        url = reverse("staffmodel-detail", kwargs={"pk": 1})

        self.client.force_login(self.user_1)

        response = self.client.patch(path=url, content_type="application/json")

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")

    def test_patch_not_logged_user_return_403(self):
        url = reverse("staffmodel-detail", kwargs={"pk": 1})

        response = self.client.patch(path=url, content_type="application/json")

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")

    def test_delete_logged_have_permissions_user_return_204(self):
        object_to_delete = StaffModel.objects.filter(username="test_2").first()
        url = reverse("staffmodel-detail", kwargs={"pk": object_to_delete.id})

        self.client.force_login(self.user_1)
        self.permission = Permission.objects.get(codename="delete_staffmodel")
        self.user_1.user_permissions.add(self.permission)

        response = self.client.delete(path=url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")

    def test_delete_logged_user_no_permissions_return_403(self):
        url = reverse("staffmodel-detail", kwargs={"pk": 1})
        self.client.force_login(self.user_1)

        response = self.client.delete(path=url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")

    def test_delete_not_logged_user_return_403(self):
        url = reverse("staffmodel-detail", kwargs={"pk": 1})

        response = self.client.delete(path=url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")
