import secrets

from django.test import TestCase, Client, tag
from django.urls import reverse
from django.contrib.auth.models import Permission
from rest_framework import status
from faker import Faker

from staff.models import StaffModel
from containers.models import Container

DETAIL_URL = "containers-create"


class ContainersCreateTest(TestCase):
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

        self.container_1 = Container.objects.create(name="Main warehouse")

    def test_get_not_logged_user_return_302(self):
        response = self.client.get(path=reverse(DETAIL_URL))

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")

    def test_get_logged_user_return_200(self):
        self.client.force_login(self.user_1)

        response = self.client.get(path=reverse(DETAIL_URL))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")

    def test_get_logged_user_have_permissions_return_200(self):
        self.client.force_login(self.user_2)

        response = self.client.get(path=reverse(DETAIL_URL))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")

    def test_post_not_logged_user_return_302(self):
        response = self.client.post(path=reverse(DETAIL_URL))

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

    @tag("test")
    def test_post_logged_user_return_200(self):
        self.client.force_login(self.user_1)

        data = {"name": "Special / Other"}
        response = self.client.post(path=reverse(DETAIL_URL), data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

    @tag("test")
    def test_post_logged_user_have_permissions_return_200(self):
        self.client.force_login(self.user_2)

        data = {"name": "Special / Other"}
        response = self.client.post(path=reverse(DETAIL_URL), data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")
