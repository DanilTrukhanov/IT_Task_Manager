from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import generic

from tasks.forms import TaskCreationForm
from tasks.models import Task


def index(request):
    return render(request, "base.html")


class TaskListView(generic.ListView):
    model = Task

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_time"] = timezone.now()
        return context


class TaskDetailView(generic.DetailView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskCreationForm
    success_url = reverse_lazy("tasks:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskCreationForm

    def get_success_url(self):
        pk = self.kwargs.get("pk")
        return reverse_lazy("tasks:task-detail", args=[pk])
