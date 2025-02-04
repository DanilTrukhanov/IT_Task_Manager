from django.shortcuts import render
from django.utils import timezone
from django.views import generic

from tasks.models import Task
from users.models import Worker


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
