from django.shortcuts import render
from django.views import generic

from users.models import Worker


class WorkerListView(generic.ListView):
    model = Worker
