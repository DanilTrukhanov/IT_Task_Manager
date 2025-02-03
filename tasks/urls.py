
from django.urls import path, include

from tasks.views import index, TaskListView

urlpatterns = [
    path("", index, name="home"),
    path("tasks/", TaskListView.as_view(), name="task-list"),

]

app_name = "tasks"
