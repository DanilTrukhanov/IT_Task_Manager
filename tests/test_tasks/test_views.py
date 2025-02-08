import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from tasks.models import Task, TaskType


class TestHomeView(TestCase):
    def test_login_required(self):
        response = self.client.get(reverse("tasks:home"))
        self.assertNotEqual(response.status_code, 200)

        user = get_user_model().objects.create_user(
            username="test",
            password="test1234",
        )
        self.client.force_login(user)
        response = self.client.get(reverse("tasks:home"))
        self.assertEqual(response.status_code, 200)


class TestTaskList(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test1234",
        )
        self.client.force_login(self.user)

        feature = TaskType.objects.create(name="Feature")
        bug = TaskType.objects.create(name="Bug")

        self.task1 = Task.objects.create(
            name="Add pagination",
            description="Add pagination to the task list",
            deadline=datetime.datetime(year=2025, month=2, day=25),
            is_completed=False,
            priority=Task.PriorityChoice.LOW,
            task_type=feature
        )
        self.task1.assignees.add(self.user)

        self.task2 = Task.objects.create(
            name="Fix login page",
            description="Do something with login page",
            deadline=datetime.datetime(year=2025, month=1, day=25),
            is_completed=True,
            priority=Task.PriorityChoice.URGENT,
            task_type=bug
        )
        self.task2.assignees.add(self.user)

    def test_task_list_order_by_status(self):
        response = self.client.get(reverse("tasks:task-list"))

        actual_result = response.context.get("task_list")
        expected_result = [self.task1, self.task2]

        self.assertEqual(list(actual_result), expected_result)

    def test_task_list_order_by_priority(self):
        self.task2.is_completed = False
        self.task2.save()

        response = self.client.get(reverse("tasks:task-list"))

        actual_result = response.context.get("task_list")
        expected_result = [self.task2, self.task1]

        self.assertEqual(list(actual_result), expected_result)

    def test_task_list_order_with_same_priority_and_status(self):
        self.task2.is_completed = False
        self.task2.priority = Task.PriorityChoice.LOW
        self.task2.save()

        response = self.client.get(reverse("tasks:task-list"))

        actual_result = response.context.get("task_list")
        expected_result = [self.task2, self.task1]

        self.assertEqual(
            list(actual_result),
            expected_result,
            "Tasks with same priority and status should be ordered by deadline"
        )

    def test_task_toggle_status(self):
        self.client.get(reverse("tasks:task-change-status", args=[self.task1.id]))
        self.client.get(reverse("tasks:task-change-status", args=[self.task2.id]))

        self.task1.refresh_from_db()
        self.task2.refresh_from_db()

        self.assertTrue(self.task1.is_completed)
        self.assertFalse(self.task2.is_completed)


    def test_task_delete(self):
        response = self.client.post(
            reverse("tasks:task-delete", kwargs={"pk": self.task1.id}),
        )

        self.assertEqual(response.status_code, 302)
        self.assertFalse(
            Task.objects.filter(id=self.task1.id).exists()
        )

    def test_task_search(self):
        response = self.client.get(
            reverse("tasks:task-list") + "?task=Pagination"
        )
        actual_response = response.context.get("task_list")
        expected = [self.task1]

        self.assertEqual(list(actual_response), expected)


class TestTaskTypeList(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test1234",
        )
        self.client.force_login(self.user)

        self.task_type1 = TaskType.objects.create(
            name="QA"
        )
        self.task_type2 = TaskType.objects.create(
            name="Bug"
        )

    def test_task_type_list_order(self):
        response = self.client.get(reverse("tasks:task-type-list"))
        actual_result = response.context.get("tasktype_list")
        expected_result = [self.task_type2, self.task_type1]

        self.assertEqual(list(actual_result), expected_result)

    def test_task_type_update(self):
        task_type_name = "Feature"
        response = self.client.post(
            reverse("tasks:task-type-update", kwargs={"pk": self.task_type1.id}),
            data={"name": task_type_name}
        )
        self.task_type1.refresh_from_db()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.task_type1.name, task_type_name)

    def test_task_type_delete(self):
        response = self.client.post(
            reverse("tasks:task-type-delete", kwargs={"pk": self.task_type1.id})
        )

        self.assertEqual(response.status_code, 302)
        self.assertFalse(
            TaskType.objects.filter(id=self.task_type1.id).exists()
        )
