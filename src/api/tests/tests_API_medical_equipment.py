import secrets

from django.contrib.auth.models import Permission
from django.test import TestCase
from containers.models import MedicalEquipment, Container
from staff.models import StaffModel
from django.urls import reverse
from rest_framework import status


class TestMedicalEquipmentResponse(TestCase):
    def setUp(self) -> None:
        self.container = Container.objects.create(name="Main core")
        self.user = StaffModel.objects.create(
            username="nimda", password=secrets.token_hex(nbytes=10)
        )
        self.medical_equipment_1 = MedicalEquipment.objects.create(name="USG")
        self.medical_equipment_2 = MedicalEquipment.objects.create(name="Filter")

    def test_get_logged_user_return_right_values_with_two_objects(self):
        url = reverse("medicalequipment-list")
        self.client.force_login(self.user)
        response = self.client.get(url)

        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["name"], "USG")
        self.assertEqual(response.data[1]["name"], "Filter")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")

    def test_get_not_logged_user_return_403(self):
        url = reverse("medicalequipment-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")

    def test_post_logged_have_permissions_user_return_405(self):
        url = reverse("medicalequipment-list")
        self.client.force_login(self.user)
        self.permission = Permission.objects.get(codename="add_medicalequipment")
        self.user.user_permissions.add(self.permission)
        data = {"name": "Thermometer"}
        response = self.client.post(path=url, data=data)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

    def test_post_logged_user_no_permissions_return_403(self):
        url = reverse("medicalequipment-list")
        self.client.force_login(self.user)
        data = {"name": "Thermometer"}
        response = self.client.post(path=url, data=data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

    def test_post_not_logged_user_return_403(self):
        url = reverse("medicalequipment-list")
        data = {"name": "Thermometer"}
        response = self.client.post(path=url, data=data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

    def test_patch_logged_have_permissions_user_return_405(self):
        url = reverse("medicalequipment-list")

        self.client.force_login(self.user)
        self.permission = Permission.objects.get(codename="change_medicalequipment")
        self.user.user_permissions.add(self.permission)

        response = self.client.patch(path=url)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")

    def test_patch_logged_user_no_permissions_return_403(self):
        url = reverse("medicalequipment-list")
        self.client.force_login(self.user)

        response = self.client.patch(path=url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")

    def test_patch_not_logged_user_return_403(self):
        url = reverse("medicalequipment-list")
        response = self.client.patch(path=url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")

    def test_delete_logged_have_permissions_user_return_405(self):
        url = reverse("medicalequipment-list")

        self.client.force_login(self.user)
        self.permission = Permission.objects.get(codename="delete_medicalequipment")
        self.user.user_permissions.add(self.permission)

        response = self.client.delete(path=url)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")

    def test_delete_logged_user_no_permissions_return_403(self):
        url = reverse("medicalequipment-list")
        self.client.force_login(self.user)

        response = self.client.delete(path=url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")

    def test_delete_not_logged_user_return_403(self):
        url = reverse("medicalequipment-list")
        response = self.client.delete(path=url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")
