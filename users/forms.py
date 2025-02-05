from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import Worker, Position


class WorkerCreationForm(UserCreationForm):
    position = forms.ModelChoiceField(
        queryset=Position.objects.all(),
        widget=forms.RadioSelect
    )

    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "position",
        )


class WorkerUpdateForm(forms.ModelForm):
    position = forms.ModelChoiceField(
        queryset=Position.objects.all(),
        widget=forms.RadioSelect
    )

    class Meta:
        model = Worker
        fields = ("first_name", "last_name", "email", "position")
