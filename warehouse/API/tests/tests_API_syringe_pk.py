from django.contrib.auth.models import Permission
from django.test import TestCase, tag
from containers.models import Syringe, Container
from staff.models import StaffModel
from django.urls import reverse
from rest_framework import status
from warehouse.env import env


class TestSyringeResponse(TestCase):
    def setUp(self) -> None:
        self.container = Container.objects.create(name="Main warehouse")
        self.user = StaffModel.objects.create(
            username="nimda", password=env("TEST_PASSWORD")
        )
        self.element_1 = Syringe.objects.create(name="Syringe", volume="1ml")
        self.element_2 = Syringe.objects.create(name="Syringe", volume="10ml")

    def test_get_not_logged_user_return_403(self):
        object_to_get = Syringe.objects.filter(name="Syringe").first()
        url = reverse("syringe-detail", kwargs={"pk": object_to_get.id})

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")

    def test_get_logged_user_return_right_values_from_object(self):
        object_to_get = Syringe.objects.filter(name="Syringe").first()
        url = reverse("syringe-detail", kwargs={"pk": object_to_get.id})

        self.client.force_login(self.user)

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")
        self.assertEqual(response.data["id"], object_to_get.id)
        self.assertEqual(response.data["name"], object_to_get.name)

    def test_get_logged_user_return_404_when_object_not_exist(self):
        url = reverse("syringe-detail", kwargs={"pk": 100000})

        self.client.force_login(self.user)

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")

    def test_post_logged_have_permissions_user_return_405(self):
        url = reverse("syringe-detail", kwargs={"pk": 1})

        self.client.force_login(self.user)
        self.permission = Permission.objects.get(codename="add_syringe")
        self.user.user_permissions.add(self.permission)

        response = self.client.post(path=url)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

    def test_post_logged_user_no_permissions_return_403(self):
        url = reverse("syringe-detail", kwargs={"pk": 1})

        self.client.force_login(self.user)

        response = self.client.post(path=url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

    def test_post_not_logged_user_return_403(self):
        url = reverse("syringe-detail", kwargs={"pk": 1})

        response = self.client.post(path=url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

    def test_patch_logged_have_permissions_user_return_right_value(self):
        object_to_patch = Syringe.objects.filter(name="Syringe").first()
        url = reverse("syringe-detail", kwargs={"pk": object_to_patch.id})

        self.client.force_login(self.user)
        self.permission = Permission.objects.get(codename="change_syringe")
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

    def test_patch_logged_have_permissions_user_invalid_name_return_400(self):
        object_to_patch = Syringe.objects.filter(name="Syringe").first()
        url = reverse("syringe-detail", kwargs={"pk": object_to_patch.id})

        self.client.force_login(self.user)
        self.permission = Permission.objects.get(codename="change_syringe")
        self.user.user_permissions.add(self.permission)

        data = {"name": "some_name", "description": "test_description"}
        response = self.client.patch(
            path=url, data=data, content_type="application/json"
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")

    def test_patch_logged_user_no_permissions_return_403(self):
        url = reverse("syringe-detail", kwargs={"pk": 1})

        self.client.force_login(self.user)

        response = self.client.patch(path=url, content_type="application/json")

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")

    def test_patch_not_logged_user_return_403(self):
        url = reverse("syringe-detail", kwargs={"pk": 1})

        response = self.client.patch(path=url, content_type="application/json")

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")

    def test_delete_logged_have_permissions_user_return_204(self):
        object_to_delete = Syringe.objects.filter(name="Syringe").first()
        url = reverse("syringe-detail", kwargs={"pk": object_to_delete.id})

        self.client.force_login(self.user)
        self.permission = Permission.objects.get(codename="delete_syringe")
        self.user.user_permissions.add(self.permission)

        response = self.client.delete(path=url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")

    def test_delete_logged_user_no_permissions_return_403(self):
        url = reverse("syringe-detail", kwargs={"pk": 1})
        self.client.force_login(self.user)

        response = self.client.delete(path=url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")

    def test_delete_not_logged_user_return_403(self):
        url = reverse("syringe-detail", kwargs={"pk": 1})

        response = self.client.delete(path=url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")
