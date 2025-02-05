from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import generic

from tasks.forms import TaskCreationForm
from tasks.models import Task, TaskType


@login_required
def index(request):
    return render(request, "base.html")


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 8

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


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:task-list")


class TaskTypeListView(LoginRequiredMixin, generic.ListView):
    model = TaskType
    template_name = "tasks/task_type_list.html"


class TaskTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = TaskType
    fields = "__all__"
    template_name = "tasks/task_type_form.html"
    success_url = reverse_lazy("tasks:task-type-list")


class TaskTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = TaskType
    fields = "__all__"
    template_name = "tasks/task_type_form.html"
    success_url = reverse_lazy("tasks:task-type-list")


class TaskTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = TaskType
    success_url = reverse_lazy("tasks:task-type-list")
    template_name = None


def toggle_status(request: HttpResponse, pk: int) -> HttpRequest:
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = not task.is_completed
    task.save()
    return redirect("tasks:task-detail", pk=pk)
