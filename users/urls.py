from django.urls import path

from tasks.views import WorkerListView


urlpatterns = [
    path("workers/", WorkerListView.as_view(), name="worker-list"),
]

app_name = "workers"
