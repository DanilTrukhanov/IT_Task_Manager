from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from users.forms import WorkerCreationForm, WorkerUpdateForm
from users.models import Worker, Position


class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker

    def get_queryset(self):
        queryset = get_user_model().objects.all()

        user_to_search = self.request.GET.get("name")
        if user_to_search:
            queryset = (
                queryset.filter(
                    Q(username__icontains=user_to_search)
                    | Q(first_name__icontains=user_to_search)
                    | Q(last_name__icontains=user_to_search)
                )
            )
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user_to_search = self.request.GET.get("name")
        if user_to_search:
            context["user_to_search"] = user_to_search
        return context


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker


class WorkerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Worker
    form_class = WorkerUpdateForm

    def get_success_url(self):
        pk = self.kwargs.get("pk")
        return reverse_lazy("workers:worker-detail", args=[pk])


class WorkerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Worker
    form_class = WorkerCreationForm
    success_url = reverse_lazy("workers:worker-list")


class WorkerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Worker
    success_url = reverse_lazy("workers:worker-list")


class PositionListView(LoginRequiredMixin, generic.ListView):
    model = Position


class PositionCreateView(LoginRequiredMixin, generic.CreateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("workers:position-list")


class PositionUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("workers:position-list")


class PositionDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Position
    success_url = reverse_lazy("workers:position-list")


class CustomLoginView(LoginView):
    template_name = "registration/login.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("tasks:home")
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        to_remember = request.POST.get("remember")
        if to_remember:
            request.session.set_expiry(604800)
        else:
            request.session.set_expiry(0)
        return super().post(request, *args, **kwargs)
