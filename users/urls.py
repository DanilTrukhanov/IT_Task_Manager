from django.urls import path, include

urlpatterns = [
    path("", workers, name="worker-list"),
]
