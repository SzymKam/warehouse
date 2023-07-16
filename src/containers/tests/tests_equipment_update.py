import secrets

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import Permission
from rest_framework import status
from faker import Faker

from staff.models import StaffModel
from containers.models import Container, MedicalEquipment

DETAIL_URL = "equipment-update"


class EquipmentUpdateTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.fake = Faker()

        self.user_1 = StaffModel.objects.create(
            username=self.fake.name(), password=secrets.token_hex(nbytes=8)
        )
        self.user_2 = StaffModel.objects.create(
            username=self.fake.name(), password=secrets.token_hex(nbytes=8)
        )

        self.user_2.user_permissions.add(Permission.objects.get(codename="add_drug"))
        self.user_2.user_permissions.add(Permission.objects.get(codename="change_drug"))
        self.user_2.user_permissions.add(Permission.objects.get(codename="delete_drug"))

        self.container_1 = Container.objects.create(name="Main core")
        self.equipment_1 = MedicalEquipment.objects.create(
            name="Filter", container=self.container_1
        )

    @staticmethod
    def detail_url(container, equipment) -> str:
        return reverse(
            DETAIL_URL,
            kwargs={
                "container": container.pk,
                "name": equipment.name,
                "pk": equipment.pk,
            },
        )

    def test_get_not_logged_user_return_302(self) -> None:
        response = self.client.get(
            path=self.detail_url(container=self.container_1, equipment=self.equipment_1)
        )

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")

    def test_get_logged_user_return_302(self) -> None:
        self.client.force_login(self.user_1)

        response = self.client.get(
            path=self.detail_url(container=self.container_1, equipment=self.equipment_1)
        )

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")

    def test_get_logged_user_have_permissions_return_200(self) -> None:
        self.client.force_login(self.user_2)

        response = self.client.get(
            path=self.detail_url(container=self.container_1, equipment=self.equipment_1)
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")

    def test_post_not_logged_user_return_302(self) -> None:
        response = self.client.post(
            path=self.detail_url(container=self.container_1, equipment=self.equipment_1)
        )

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

    def test_post_logged_user_return_302(self) -> None:
        self.client.force_login(self.user_1)
        response = self.client.post(
            path=self.detail_url(container=self.container_1, equipment=self.equipment_1)
        )

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

    def test_post_logged_user_have_permissions_return_200(self) -> None:
        self.client.force_login(self.user_2)
        response = self.client.post(
            path=self.detail_url(container=self.container_1, equipment=self.equipment_1)
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

    def test_patch_not_logged_user_return_302(self) -> None:
        response = self.client.patch(
            path=self.detail_url(container=self.container_1, equipment=self.equipment_1)
        )

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")

    def test_patch_logged_user_return_302(self) -> None:
        self.client.force_login(self.user_1)
        response = self.client.patch(
            path=self.detail_url(container=self.container_1, equipment=self.equipment_1)
        )

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")

    def test_patch_logged_user_have_permissions_return_200(self) -> None:
        self.client.force_login(self.user_2)
        response = self.client.patch(
            path=self.detail_url(container=self.container_1, equipment=self.equipment_1)
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")

    def test_delete_not_logged_user_return_302(self) -> None:
        response = self.client.delete(
            path=self.detail_url(container=self.container_1, equipment=self.equipment_1)
        )

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")

    def test_delete_logged_user_return_302(self) -> None:
        self.client.force_login(self.user_1)
        response = self.client.delete(
            path=self.detail_url(container=self.container_1, equipment=self.equipment_1)
        )

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")

    def test_delete_logged_user_have_permissions_return_302(self) -> None:
        self.client.force_login(self.user_2)
        response = self.client.delete(
            path=self.detail_url(container=self.container_1, equipment=self.equipment_1)
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")
