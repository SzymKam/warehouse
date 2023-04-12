from __future__ import annotations
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
    CreateView,
)
from .models import Container, MedicalEquipment
from .forms import ContainerForm, MedicalEquipmentForm, DrugForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponse
from .constants import MEDICAL_EQUIPMENT_NAME_CHOICES


def warehouse_main(request):
    """render main warehouse page"""
    return render(
        request, "containers/warehouse-main.html", {"title": "Main Warehouse"}
    )


class BaseContainer:
    model = Container
    success_url = reverse_lazy("containers-home")


class ContainerView(ListView):
    queryset = Container.objects.all()
    template_name = "containers/containers-home.html"

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ContainerDetail(DetailView):
    template_name = "containers/containers-detail.html"
    queryset = Container.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["equipment"] = MedicalEquipment.objects.filter(container=self.object.id)
        return context


class ContainerUpdate(UpdateView):
    model = Container
    template_name = "containers/containers-update.html"
    form_class = ContainerForm

    def get_success_url(self):
        return reverse_lazy("containers-detail", args=(self.object.id,))

    def form_valid(self, form):
        messages.info(self.request, "Container updated!")
        return super().form_valid(form)


class ContainerCreate(BaseContainer, CreateView):
    template_name = "containers/containers-create.html"
    form_class = ContainerForm

    queryset = Container.objects.all()

    def form_valid(self, form):
        messages.success(self.request, "Container crated!")
        return super().form_valid(form)


class ContainerDelete(BaseContainer, DeleteView):
    template_name = "containers/containers-delete.html"

    def form_valid(self, form):
        messages.warning(self.request, "Container deleted!")
        return super().form_valid(form)


class MedicalEquipmentCreate(CreateView):
    template_name = "equipment/equipment-create.html"
    model = MedicalEquipment
    queryset = MedicalEquipment.objects.all()
    success_url = reverse_lazy("containers-home")
    form_class = MedicalEquipmentForm

    def form_valid(self, form):
        messages.success(self.request, "Equipment added")
        return super().form_valid(form)


class MedicalEquipmentDelete(DeleteView):
    model = MedicalEquipment
    success_url = reverse_lazy("containers-home")
    template_name = "equipment/equipment-delete.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["container"] = self.object.container
        print(context["container"])
        return context


def get_name(request):
    if request.method == "POST":
        name = request.POST["name"]
        return render(request, "equipment/equipment-create-2nd.html", {"name": name})
    return render(
        request,
        "equipment/equipment-create-2nd.html",
        {"name_choices": MEDICAL_EQUIPMENT_NAME_CHOICES},
    )


from .constants import DRUGS


def select_object_to_create(request, name: str):
    if name == "ASA":
        form = DrugForm(request.POST, initial={"name": name})
    else:
        form = MedicalEquipmentForm(request.POST, initial={"name": name})

    if form.is_valid() and request.method == "POST":
        print(form.data)
        return HttpResponse("Object added")
    return render(request, "equipment/equipment-create-2nd.html", {"form": form})
