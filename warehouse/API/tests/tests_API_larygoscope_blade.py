from django.contrib.auth.models import Permission
from django.test import TestCase, tag
from containers.models import LaryngoscopeBlade, Container
from staff.models import StaffModel
from django.urls import reverse
from rest_framework import status
from warehouse.env import env


class TestLaryngoscopeBladeResponse(TestCase):
    def setUp(self) -> None:
        self.container = Container.objects.create(name="Main warehouse")
        self.user = StaffModel.objects.create(
            username="nimda", password=env("TEST_PASSWORD")
        )
        self.element_1 = LaryngoscopeBlade.objects.create(
            name="Laryngoscope blade", size="0"
        )
        self.element_2 = LaryngoscopeBlade.objects.create(
            name="Laryngoscope blade", size="5"
        )

    def test_get_logged_user_return_right_values_with_two_objects(self):
        url = reverse("laryngoscopeblade-list")
        self.client.force_login(self.user)
        response = self.client.get(url)

        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["name"], self.element_1.name)
        self.assertEqual(response.data[0]["size"], self.element_1.size)

        self.assertEqual(response.data[1]["name"], self.element_2.name)
        self.assertEqual(response.data[1]["size"], self.element_2.size)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")

    def test_get_not_logged_user_return_403(self):
        url = reverse("laryngoscopeblade-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")

    def test_post_logged_have_permissions_user_return_405(self):
        url = reverse("laryngoscopeblade-list")
        self.client.force_login(self.user)
        self.permission = Permission.objects.get(codename="add_laryngoscopeblade")
        self.user.user_permissions.add(self.permission)

        response = self.client.post(path=url)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

    def test_post_logged_user_no_permissions_return_403(self):
        url = reverse("laryngoscopeblade-list")
        self.client.force_login(self.user)

        response = self.client.post(path=url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

    def test_post_not_logged_user_return_403(self):
        url = reverse("laryngoscopeblade-list")

        response = self.client.post(path=url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

    def test_patch_logged_have_permissions_user_return_405(self):
        url = reverse("laryngoscopeblade-list")

        self.client.force_login(self.user)
        self.permission = Permission.objects.get(codename="change_laryngoscopeblade")
        self.user.user_permissions.add(self.permission)

        response = self.client.patch(path=url)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")

    def test_patch_logged_user_no_permissions_return_403(self):
        url = reverse("laryngoscopeblade-list")
        self.client.force_login(self.user)

        response = self.client.patch(path=url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")

    def test_patch_not_logged_user_return_403(self):
        url = reverse("laryngoscopeblade-list")
        response = self.client.patch(path=url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")

    def test_delete_logged_have_permissions_user_return_405(self):
        url = reverse("laryngoscopeblade-list")

        self.client.force_login(self.user)
        self.permission = Permission.objects.get(codename="delete_laryngoscopeblade")
        self.user.user_permissions.add(self.permission)

        response = self.client.delete(path=url)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")

    def test_delete_logged_user_no_permissions_return_403(self):
        url = reverse("laryngoscopeblade-list")
        self.client.force_login(self.user)

        response = self.client.delete(path=url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")

    def test_delete_not_logged_user_return_403(self):
        url = reverse("laryngoscopeblade-list")
        response = self.client.delete(path=url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")
