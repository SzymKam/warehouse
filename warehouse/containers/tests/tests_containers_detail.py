import secrets

from django.test import TestCase, Client, tag
from django.urls import reverse
from django.contrib.auth.models import Permission
from rest_framework import status
from faker import Faker

from staff.models import StaffModel


DETAIL_URL = "admin-update"


class StaffUpdateByAdminTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.fake = Faker()

        self.user_1 = StaffModel.objects.create(
            username=self.fake.name(), password=secrets.token_hex(nbytes=8)
        )
        self.user_2 = StaffModel.objects.create(
            username=self.fake.name(), password=secrets.token_hex(nbytes=8)
        )
        self.user_3 = StaffModel.objects.create(
            username=self.fake.name(), password=secrets.token_hex(nbytes=8)
        )

        self.template_used = "staff/delete.html"

        self.user_1.user_permissions.add(
            Permission.objects.get(codename="add_staffmodel")
        )
        self.user_1.user_permissions.add(
            Permission.objects.get(codename="change_staffmodel")
        )
        self.user_1.user_permissions.add(
            Permission.objects.get(codename="delete_staffmodel")
        )

    @staticmethod
    def detail_url(obj):
        return reverse(DETAIL_URL, kwargs={"pk": obj.pk})
