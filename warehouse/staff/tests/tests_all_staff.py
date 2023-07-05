import secrets

from django.test import TestCase, Client, tag
from django.urls import reverse
from staff.models import StaffModel
from warehouse.env import env


class AllStaffViewTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.url = reverse("all-staff")

        self.user_1 = StaffModel.objects.create(
            username="nimda", password=secrets.token_hex(nbytes=10)
        )
        self.user_2 = StaffModel.objects.create(
            username="test_2", password=secrets.token_hex(nbytes=10)
        )
        self.user_3 = StaffModel.objects.create(
            username="test_3", password=secrets.token_hex(nbytes=10)
        )

    def test_get_not_logged_user_return_302(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")

    def test_get_logged_user_return_staffs(self):
        self.client.force_login(self.user_1)

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")

        self.assertEqual(len(response.context["object_list"]), 3)
        self.assertIsInstance(response.context["object_list"][0], StaffModel)
        self.assertTemplateUsed(response, "staff/staff-all.html")
        self.assertTemplateUsed(response, "containers/base.html")

        self.assertEqual(response.context["title"], "GRM People")

    def test_post_logged_user_return_405(self):
        self.client.force_login(self.user_1)

        response = self.client.post(self.url)

        self.assertEqual(response.status_code, 405)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

    def test_post_not_logged_user_return_302(self):
        response = self.client.post(self.url)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")

    def test_patch_logged_user_return_405(self):
        self.client.force_login(self.user_1)

        response = self.client.patch(self.url)

        self.assertEqual(response.status_code, 405)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")

    def test_patch_not_logged_user_return_302(self):
        response = self.client.patch(self.url)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.request["REQUEST_METHOD"], "PATCH")

    def test_delete_logged_user_return_405(self):
        self.client.force_login(self.user_1)

        response = self.client.delete(self.url)

        self.assertEqual(response.status_code, 405)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")

    def test_delete_not_logged_user_return_302(self):
        response = self.client.delete(self.url)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.request["REQUEST_METHOD"], "DELETE")
