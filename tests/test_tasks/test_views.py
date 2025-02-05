from django.test import TestCase
from django.urls import reverse


class TestHomeView(TestCase):
    def test_login_required(self):
        response = self.client.get(reverse("tasks:home"))
        self.assertNotEqual(response.status_code, 200)


class TestTaskList(TestCase):
    pass