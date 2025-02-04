from django import forms

from tasks.models import Task


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
    class Meta:
        model = Task
        fields = "__all__"