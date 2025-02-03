
from django.urls import path, include

from tasks.views import index

urlpatterns = [
    path("", index, name="home"),
]

app_name = "tasks"
