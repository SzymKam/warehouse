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
            username="nimda", password=env("TEST_PASSWORD")
        )
        self.container_1 = Container.objects.create(name="Main warehouse")
        self.container_2 = Container.objects.create(name="Special/Other")

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
