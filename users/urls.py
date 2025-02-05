from django.urls import path

from users.views import WorkerListView, PositionListView, PositionDeleteView, PositionUpdateView, PositionCreateView, \
    WorkerDetailView

urlpatterns = [
    path("", WorkerListView.as_view(), name="worker-list"),
    path("<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"),
    path("positions/", PositionListView.as_view(), name="position-list"),
    path("positions/create/", PositionCreateView.as_view(), name="position-create"),
    path("positions/<int:pk>/update/", PositionUpdateView.as_view(), name="position-update"),
    path("positions/<int:pk>/delete/", PositionDeleteView.as_view(), name="position-delete"),
]

app_name = "workers"
