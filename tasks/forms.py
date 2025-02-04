import datetime

from django import forms
from django.contrib.auth import get_user_model
from django.utils import timezone

from tasks.models import Task, TaskType
from users.models import Worker


class TaskCreationForm(forms.ModelForm):
    description = forms.CharField(
        label="",
        widget=forms.Textarea(
            attrs={
                "rows": 3,
                "cols": 50,
                "placeholder": "Enter task description...",
            }
        ),
    )

    deadline = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "class": "form-control",
                "type": "date",
            }
        )
    )
    is_completed = forms.BooleanField(
        widget = forms.CheckboxInput(
            attrs={
                "class": "form-check-input",
            }
        )
    )

    task_type = forms.ModelChoiceField(
        queryset=TaskType.objects.all(),
        widget=forms.RadioSelect
    )

    priority = forms.ChoiceField(
        choices=Task.PriorityChoice,
        widget=forms.RadioSelect
    )

    assignees = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Task
        fields = "__all__"
