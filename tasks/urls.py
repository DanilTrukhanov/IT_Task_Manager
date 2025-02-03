
from django.urls import path, include

from tasks.views import index, TaskListView, TaskDetailView

urlpatterns = [
    path("", index, name="home"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),

]

app_name = "tasks"
