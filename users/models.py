from django.contrib.auth.models import AbstractUser
from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ["name"]


class Worker(AbstractUser):
    position = models.ForeignKey(Position, null=True, on_delete=models.CASCADE, related_name="workers")

    class Meta:
        ordering = ["username"]