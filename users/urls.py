from django.urls import path

from users.views import WorkerListView


urlpatterns = [
    path("", WorkerListView.as_view(), name="worker-list"),
]

app_name = "workers"
