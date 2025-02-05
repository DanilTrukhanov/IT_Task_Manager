from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from users.models import Worker, Position


class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker


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


class CustomLogoutView(LogoutView):
    next_page = "/"