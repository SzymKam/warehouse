import secrets

from django.contrib.auth.models import Permission
from django.test import TestCase
from containers.models import Fluid, Container
from staff.models import StaffModel
from django.urls import reverse
from rest_framework import status


class TestFluidResponse(TestCase):
    def setUp(self) -> None:
        self.container = Container.objects.create(name="Main core")
        self.user = StaffModel.objects.create(
            username="nimda", password=secrets.token_hex(nbytes=10)
        )
        self.drug_1 = Fluid.objects.create(name="NaCl 0.9%", volume="100ml")
        self.drug_2 = Fluid.objects.create(name="Optilyte", volume="500ml")

    def test_get_logged_user_return_right_values_with_two_objects(self):
        url = reverse("fluid-list")
        self.client.force_login(self.user)
        response = self.client.get(url)

        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["name"], "NaCl 0.9%")
        self.assertEqual(response.data[0]["volume"], "100ml")

        self.assertEqual(response.data[1]["name"], "Optilyte")
        self.assertEqual(response.data[1]["volume"], "500ml")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")

    def test_get_not_logged_user_return_403(self):
        url = reverse("fluid-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")

    def test_post_logged_have_permissions_user_return_405(self):
        url = reverse("fluid-list")
        self.client.force_login(self.user)
        self.permission = Permission.objects.get(codename="add_fluid")
        self.user.user_permissions.add(self.permission)
        data = {"name": "Plasmalyte", "volume": "100ml"}
        response = self.client.post(path=url, data=data)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

    def test_post_logged_user_no_permissions_return_403(self):
        url = reverse("fluid-list")
        self.client.force_login(self.user)
        data = {"name": "Plasmalyte", "volume": "100ml"}
        response = self.client.post(path=url, data=data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

    def test_post_not_logged_user_return_403(self):
        url = reverse("fluid-list")
        data = {"name": "Plasmalyte", "volume": "100ml"}
        response = self.client.post(path=url, data=data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

    def test_patch_logged_have_permissions_user_return_405(self):
        url = reverse("fluid-list")

        self.client.force_login(self.user)
        self.permission = Permission.objects.get(codename="change_fluid")
        self.user.user_permissions.add(self.permission)

        response = self.client.patch(path=url)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")

    def test_patch_logged_user_no_permissions_return_403(self):
        url = reverse("fluid-list")
        self.client.force_login(self.user)

        response = self.client.patch(path=url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")

    def test_patch_not_logged_user_return_403(self):
        url = reverse("fluid-list")
        response = self.client.patch(path=url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")

    def test_delete_logged_have_permissions_user_return_405(self):
        url = reverse("fluid-list")

        self.client.force_login(self.user)
        self.permission = Permission.objects.get(codename="delete_fluid")
        self.user.user_permissions.add(self.permission)

        response = self.client.delete(path=url)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")

    def test_delete_logged_user_no_permissions_return_403(self):
        url = reverse("fluid-list")
        self.client.force_login(self.user)

        response = self.client.delete(path=url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")

    def test_delete_not_logged_user_return_403(self):
        url = reverse("fluid-list")
        response = self.client.delete(path=url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")
