from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models import Worker


class TaskType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    class PriorityChoice(models.IntegerChoices):
        URGENT = 0, _("Urgent")
        HIGH = 1, _("High")
        MEDIUM = 2, _("Medium")
        LOW = 3, _("Low")

    name = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateField()
    is_completed = models.BooleanField(default=False)
    priority = models.IntegerField(choices=PriorityChoice, default=PriorityChoice.MEDIUM)
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE, related_name="tasks")
    assignees = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="tasks")

    class Meta:
        ordering = ["priority", "deadline"]
