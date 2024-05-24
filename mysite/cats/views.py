from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from cats.models import Breed, Cat
from django.urls import reverse_lazy

# Create your views here.
class CatList(LoginRequiredMixin, ListView):
    model = Cat

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        breed_count = Breed.objects.count()
        ctx["breed_count"] = breed_count
        return ctx

class CatCreate(LoginRequiredMixin, CreateView):
    model = Cat
    fields ="__all__"
    success_url =  reverse_lazy("cats:all")

class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    fields ="__all__"
    success_url =  reverse_lazy("cats:all")

class CatDelete(LoginRequiredMixin, DeleteView):
    model=Cat
    fields = "__all__"
    success_url = reverse_lazy("cats:all")

class BreedList(LoginRequiredMixin, ListView):
    model = Breed


class BreedCreate(LoginRequiredMixin, CreateView):
    model = Breed
    fields ="__all__"
    success_url =  reverse_lazy("cats:all")

class BreedUpdate(LoginRequiredMixin, UpdateView):
    model = Breed
    fields ="__all__"
    success_url =  reverse_lazy("cats:all")

class BreedDelete(LoginRequiredMixin, DeleteView):
    model = Breed
    fields ="__all__"
    success_url =  reverse_lazy("cats:all")