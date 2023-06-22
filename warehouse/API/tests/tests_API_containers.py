from django.contrib.auth.models import Permission
from django.test import TestCase, tag
from containers.models import Drug, Container
from staff.models import StaffModel
from django.urls import reverse
from rest_framework import status
from warehouse.env import env


@tag("test")
class TestContainersResponse(TestCase):
    def setUp(self) -> None:
        self.user = StaffModel.objects.create(
            username="nimda", password=env("TEST_PASSWORD")
        )
        self.container_1 = Container.objects.create(name="Main warehouse")
        self.container_2 = Container.objects.create(name="Special/Other")

    def test_get_not_logged_user_return_403(self):
        url = reverse("container-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")

    def test_get_logged_user_no_permissions_return_right_value(self):
        url = reverse("container-list")
        self.client.force_login(self.user)

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]["name"], self.container_1.name)
        self.assertEqual(response.data[1]["name"], self.container_2.name)
        self.assertEqual(response.data[0]["id"], self.container_1.id)
        self.assertEqual(response.data[1]["id"], self.container_2.id)
        self.assertEqual(response.data[0]["description"], self.container_1.description)
        self.assertEqual(response.data[1]["description"], self.container_2.description)


"""
/API/containers/	API.views.containers_crud_API.ContainersViewSet	container-list
/API/containers/<pk>/	API.views.containers_crud_API.ContainersViewSet	container-detail
"""
