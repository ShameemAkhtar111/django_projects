from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from autos.models import Make,Autos
from django.views import View
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from autos.forms import MakeForm
# Create your views here.

class MainView(LoginRequiredMixin, ListView):
    model = Autos
    # template_name = "autos/auto_list.html"    #it will take by default name as modelname_list i.e autos_list.html
    context_object_name = "auto_list"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        mc = Make.objects.count()
        context["make_count"] = mc
        return context

class MakeView(LoginRequiredMixin, ListView):
    model = Make


class MakeCreate(LoginRequiredMixin, View):
    template = "autos/make_form.html"
    success_url = reverse_lazy("autos:all")

    def get(self,request):
        form = MakeForm()
        ctx = {'form':form}
        return render(request,self.template,ctx)

    def post(self,request):
        form=MakeForm(request.POST)
        if not form.is_valid():
            ctx = {'form':form}
            return render(request,self.template,ctx)
        form.save()
        return redirect(self.success_url)

class MakeUpdate(LoginRequiredMixin, View):
    model = Make
    template = "autos/make_form.html"
    success_url = reverse_lazy("autos:all")
    
    def get(self, request,pk):
        make = get_object_or_404(self.model,pk=pk)
        form = MakeForm(instance=make)
        ctx = {"form":form}
        return render(request,self.template,ctx)

    def post(self,request,pk):
        make = get_object_or_404(self.model, pk=pk)
        form = MakeForm(request.POST, instance=make)
        if not form.is_valid():
            ctx = {"form":form}
            return render(request,self.template,ctx)
        
        form.save()
        return redirect(self.success_url)

class MakeDelete(LoginRequiredMixin, View):
    model = Make
    template = "autos/make_confirm_delete.html"
    success_url = reverse_lazy('autos:all')

    def get(self, request, pk):
        make = get_object_or_404(self.model, pk=pk)
        ctx = {"make": make}
        return render(request, self.template, ctx)
    
    def post(self, request, pk):
        make = get_object_or_404(self.model, pk=pk)
        make.delete()
        return redirect(self.success_url)

class AutoCreate(LoginRequiredMixin, CreateView):
    model= Autos
    fields = "__all__"
    success_url = reverse_lazy("autos:all")

class AutoUpdate(LoginRequiredMixin, UpdateView):
    model = Autos
    fields = "__all__"
    success_url = reverse_lazy("autos:all")

class AutoDelete(LoginRequiredMixin, DeleteView):
    model = Autos
    fields = '__all__'
    success_url = reverse_lazy('autos:all')

    
