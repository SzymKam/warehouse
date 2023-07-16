import secrets

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import Permission
from rest_framework import status
from faker import Faker

from staff.models import StaffModel
from containers.models import Container

DETAIL_URL = "containers-update"


class ContainersUpdateTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.fake = Faker()

        self.user_1 = StaffModel.objects.create(
            username=self.fake.name(), password=secrets.token_hex(nbytes=8)
        )
        self.user_2 = StaffModel.objects.create(
            username=self.fake.name(), password=secrets.token_hex(nbytes=8)
        )

        self.user_2.user_permissions.add(
            Permission.objects.get(codename="add_container")
        )
        self.user_2.user_permissions.add(
            Permission.objects.get(codename="change_container")
        )
        self.user_2.user_permissions.add(
            Permission.objects.get(codename="delete_container")
        )

        self.container_1 = Container.objects.create(name="Main core")

        self.container_2 = Container.objects.create(name="Trauma Wall - ALS")

    @staticmethod
    def detail_url(obj) -> str:
        return reverse(DETAIL_URL, kwargs={"pk": obj.pk})

    def test_get_not_logged_user_return_302(self) -> None:
        response = self.client.get(path=self.detail_url(self.container_1))

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")

    def test_get_logged_user_return_200(self) -> None:
        self.client.force_login(self.user_1)

        response = self.client.get(path=self.detail_url(self.container_1))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")
        self.assertTemplateUsed("containers/containers-update.html")

    def test_get_logged_user_have_permissions_return_200(self) -> None:
        self.client.force_login(self.user_2)

        response = self.client.get(path=self.detail_url(self.container_1))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")
        self.assertEqual(response.context["object"], self.container_1)
        self.assertTemplateUsed("containers/containers-update.html")

    def test_post_not_logged_user_return_302(self) -> None:
        response = self.client.post(path=self.detail_url(self.container_1))

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

    def test_post_logged_user_return_200_not_update(self) -> None:
        self.client.force_login(self.user_1)

        data = {"description": "updated container"}
        response = self.client.post(path=self.detail_url(self.container_1), data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")
        self.assertTemplateUsed("containers/containers-update.html")

    def test_post_logged_user_have_permissions_return_200(self) -> None:
        self.client.force_login(self.user_2)

        data = {"description": "updated container"}
        response = self.client.post(path=self.detail_url(self.container_1), data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")
        self.assertTemplateUsed("containers/containers-detail.html")
        self.assertEqual(response.context["object"].description, data["description"])

    def test_patch_not_logged_user_return_302(self) -> None:
        response = self.client.patch(path=self.detail_url(self.container_1))

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")

    def test_patch_logged_user_return_200(self) -> None:
        self.client.force_login(self.user_1)

        data = {"description": "updated container"}
        response = self.client.patch(path=self.detail_url(self.container_1), data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")
        self.assertTemplateUsed("containers/containers-update.html")

    def test_patch_logged_user_have_permissions_return_405(self) -> None:
        self.client.force_login(self.user_2)

        data = {"description": "updated container"}
        response = self.client.patch(path=self.detail_url(self.container_1), data=data)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")
        self.assertTemplateUsed("containers/containers-update.html")

    def test_delete_not_logged_user_return_302(self) -> None:
        response = self.client.delete(path=self.detail_url(self.container_1))

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")

    def test_delete_logged_user_return_200(self) -> None:
        self.client.force_login(self.user_1)

        response = self.client.delete(path=self.detail_url(self.container_1))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")
        self.assertTemplateUsed("containers/containers-update.html")

    def test_delete_logged_user_have_permissions_return_200(self) -> None:
        self.client.force_login(self.user_2)

        response = self.client.delete(path=self.detail_url(self.container_1))

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")
        self.assertTemplateUsed("containers/containers-update.html")
