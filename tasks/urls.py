
from django.urls import path, include

from tasks.views import (
    index,
    TaskListView,
    TaskDetailView,
    TaskCreateView, TaskUpdateView
)

urlpatterns = [
    path("", index, name="home"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),

]

app_name = "tasks"
