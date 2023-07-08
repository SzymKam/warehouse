from django.test import TestCase, Client, tag
from django.urls import reverse


class PasswordResetCompleteTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.url = reverse("password_reset_complete")

    def test_if_get_return_right_values(self):
        response = self.client.get(self.url)

        self.assertTemplateUsed(response, "staff/password-reset-done.html")
        self.assertEqual(response.context["subtitle"], "Password reset done")
        self.assertEqual(response.context["title"], "GRM Password reset done")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")

    def test_if_post_return_405(self):
        response = self.client.post(self.url)

        self.assertEqual(response.status_code, 405)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")


class PasswordResetDoneViewTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.url = reverse("password_reset_done")

    def test_if_get_return_right_values(self):
        response = self.client.get(self.url)

        self.assertTemplateUsed(response, "staff/password-reset-sent.html")
        self.assertEqual(response.context["subtitle"], "Password reset sent")
        self.assertEqual(response.context["title"], "GRM Password reset sent")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")

    def test_if_post_return_405(self):
        response = self.client.post(self.url)

        self.assertEqual(response.status_code, 405)
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")


class PasswordResetViewTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.url = reverse("reset-password")

    def test_if_get_return_right_values(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "staff/password-reset.html")
        self.assertEqual(response.context["subtitle"], "Reset Password")
        self.assertEqual(response.context["title"], "GRM Password reset")
        self.assertEqual(response.request["REQUEST_METHOD"], "GET")

    def test_if_post_return_right_values(self):
        response = self.client.post(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "staff/password-reset.html")
        self.assertEqual(response.context["subtitle"], "Reset Password")
        self.assertEqual(response.context["title"], "GRM Password reset")
        self.assertEqual(response.request["REQUEST_METHOD"], "POST")
