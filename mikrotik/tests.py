from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from .models import MikrotikDevice


class DeviceListViewTest(TestCase):
    def setUp(self):
        MikrotikDevice.objects.create(
            name="Router1", ip_address="192.168.88.1", username="admin", password="pass"
        )

    def test_device_list_view(self):
        response = self.client.get(reverse("device_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Router1")


class UserListViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="tester", password="pass")

    def test_requires_login(self):
        response = self.client.get(reverse("user_list"))
        self.assertEqual(response.status_code, 302)
        self.assertIn("/accounts/login/", response["Location"])

    def test_view_with_login(self):
        self.client.login(username="tester", password="pass")
        response = self.client.get(reverse("user_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "tester")


class LoginViewTest(TestCase):
    def test_login_page_loads(self):
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)
