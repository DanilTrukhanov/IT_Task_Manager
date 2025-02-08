from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from users.models import Position


class TestWorkerList(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test1234",
        )
        self.client.force_login(self.user)

    def test_worker_update(self):
        position = Position.objects.create(name="Developer")
        new_usernmae = "testusername"
        response = self.client.post(
            reverse("workers:worker-update", kwargs={"pk": self.user.id}),
            data={
                "username": new_usernmae,
                "position": position.id
            }
        )

        self.user.refresh_from_db()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.user.username, new_usernmae)

    def test_worker_delete(self):
        response = self.client.post(
            reverse("workers:worker-delete", kwargs={"pk": self.user.id})
        )

        self.assertEqual(response.status_code, 302)
        self.assertFalse(
            get_user_model().objects.filter(id=self.user.id).exists()
        )

    def test_worker_search(self):
        user1 = get_user_model().objects.create_user(
            username="Jason",
            password="test1234",
        )

        response = self.client.get(
            reverse("workers:worker-list") + "?name=Jason"
        )

        actual_result = response.context.get("worker_list")
        expected = [user1]

        self.assertEqual(list(actual_result), expected)


class TestPositionList(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test1234",
        )
        self.client.force_login(self.user)

        self.position1 = Position.objects.create(name="Project Manager")
        self.position2 = Position.objects.create(name="BIG BOSS")


    def test_position_list_order(self):
        response = self.client.get(reverse("workers:position-list"))

        actual_result = response.context.get("position_list")
        expected_result = [self.position2, self.position1]

        self.assertEqual(list(actual_result), expected_result)

    def test_position_update(self):
        new_position_name = "ALSO BIG BOSS"

        response = self.client.post(
            reverse("workers:position-update", kwargs={"pk": self.position1.id}),
            data={"name": new_position_name}
        )
        self.position1.refresh_from_db()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.position1.name, new_position_name)

    def test_position_delete(self):
        response = self.client.post(
            reverse("workers:position-delete", kwargs={"pk": self.position2.id})
        )

        self.assertEqual(response.status_code, 302)
        self.assertFalse(
            Position.objects.filter(id=self.position2.id).exists()
        )