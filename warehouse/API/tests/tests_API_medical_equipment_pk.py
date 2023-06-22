from django.contrib.auth.models import Permission
from django.test import TestCase, tag
from containers.models import MedicalEquipment, Container
from staff.models import StaffModel
from django.urls import reverse
from rest_framework import status
from warehouse.env import env


class TestMedicalEquipmentResponse(TestCase):
    def setUp(self) -> None:
        self.container = Container.objects.create(name="Main warehouse")
        self.user = StaffModel.objects.create(
            username="nimda", password=env("TEST_PASSWORD")
        )
        self.medical_equipment_1 = MedicalEquipment.objects.create(name="USG")
        self.medical_equipment_2 = MedicalEquipment.objects.create(name="Filter")

    @tag("API-medicalequipment-get-id")
    def test_get_not_logged_user_return_403(self):
        object_to_get = MedicalEquipment.objects.filter(name="USG").first()
        url = reverse("medicalequipment-detail", kwargs={"pk": object_to_get.id})

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")

    @tag("API-medicalequipment-get-id")
    def test_get_logged_user_return_right_values_from_object(self):
        object_to_get = MedicalEquipment.objects.filter(name="USG").first()
        url = reverse("medicalequipment-detail", kwargs={"pk": object_to_get.id})

        self.client.force_login(self.user)

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")
        self.assertEqual(response.data["id"], object_to_get.id)
        self.assertEqual(response.data["name"], object_to_get.name)

    @tag("API-medicalequipment-get-id")
    def test_get_logged_user_return_404_when_object_not_exist(self):
        url = reverse("medicalequipment-detail", kwargs={"pk": 100000})

        self.client.force_login(self.user)

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")

    @tag("API-medicalequipment-post-id")
    def test_post_logged_have_permissions_user_return_405(self):
        url = reverse("medicalequipment-detail", kwargs={"pk": 1})

        self.client.force_login(self.user)
        self.permission = Permission.objects.get(codename="add_medicalequipment")
        self.user.user_permissions.add(self.permission)

        data = {"name": "KED"}
        response = self.client.post(path=url, data=data)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

    @tag("API-medicalequipment-post-id")
    def test_post_logged_user_no_permissions_return_403(self):
        url = reverse("medicalequipment-detail", kwargs={"pk": 1})

        self.client.force_login(self.user)

        data = {"name": "KED"}
        response = self.client.post(path=url, data=data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

    @tag("API-medicalequipment-post-id")
    def test_post_not_logged_user_return_403(self):
        url = reverse("medicalequipment-detail", kwargs={"pk": 1})

        data = {"name": "KED"}
        response = self.client.post(path=url, data=data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

    @tag("API-medicalequipment-patch-id")
    def test_patch_logged_have_permissions_user_return_right_value(self):
        object_to_patch = MedicalEquipment.objects.filter(name="USG").first()
        url = reverse("medicalequipment-detail", kwargs={"pk": object_to_patch.id})

        self.client.force_login(self.user)
        self.permission = Permission.objects.get(codename="change_medicalequipment")
        self.user.user_permissions.add(self.permission)

        data = {"description": "test_description"}
        response = self.client.patch(
            path=url, data=data, content_type="application/json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")
        self.assertEqual(response.data["id"], object_to_patch.id)
        self.assertEqual(response.data["name"], object_to_patch.name)
        self.assertEqual(response.data["description"], data["description"])

    @tag("API-medicalequipment-patch-id")
    def test_patch_logged_have_permissions_user_invalid_name_return_400(self):
        object_to_patch = MedicalEquipment.objects.filter(name="USG").first()
        url = reverse("medicalequipment-detail", kwargs={"pk": object_to_patch.id})

        self.client.force_login(self.user)
        self.permission = Permission.objects.get(codename="change_medicalequipment")
        self.user.user_permissions.add(self.permission)

        data = {"name": "some_name", "description": "test_description"}
        response = self.client.patch(
            path=url, data=data, content_type="application/json"
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")

    @tag("API-medicalequipment-patch-id")
    def test_patch_logged_user_no_permissions_return_403(self):
        url = reverse("medicalequipment-detail", kwargs={"pk": 1})

        self.client.force_login(self.user)

        response = self.client.patch(path=url, content_type="application/json")

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")

    @tag("API-medicalequipment-patch-id")
    def test_patch_not_logged_user_return_403(self):
        url = reverse("medicalequipment-detail", kwargs={"pk": 1})

        response = self.client.patch(path=url, content_type="application/json")

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")

    @tag("API-medicalequipment-delete-id")
    def test_delete_logged_have_permissions_user_return_204(self):
        object_to_delete = MedicalEquipment.objects.filter(name="USG").first()
        url = reverse("medicalequipment-detail", kwargs={"pk": object_to_delete.id})

        self.client.force_login(self.user)
        self.permission = Permission.objects.get(codename="delete_medicalequipment")
        self.user.user_permissions.add(self.permission)

        response = self.client.delete(path=url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")

    @tag("API-medicalequipment-delete-id")
    def test_delete_logged_user_no_permissions_return_403(self):
        url = reverse("medicalequipment-detail", kwargs={"pk": 1})
        self.client.force_login(self.user)

        response = self.client.delete(path=url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")

    @tag("API-medicalequipment-delete-id")
    def test_delete_not_logged_user_return_403(self):
        url = reverse("medicalequipment-detail", kwargs={"pk": 1})

        response = self.client.delete(path=url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")
