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
from .forms import (
    ContainerForm,
    MedicalEquipmentForm,
    DrugFormset,
    MedicalEquipmentFormset,
    EquipmentNameForm,
)
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


def create_or_edit(request):
    return render(
        request,
        "equipment/equipment-create-2nd.html",
        {"name_choices": MEDICAL_EQUIPMENT_NAME_CHOICES},
    )


#     equipment_name_form = EquipmentNameForm(request.POST or None)
#     name = request.POST.get("name")
#     if name == "ASA":
#         special_form = DrugFormset(request.POST or None)
#         return render(request, "equipment/equipment-create-2nd.html", {"equipment_name_form": equipment_name_form,
#                                                                        "special_form": special_form})
#     return render(request, "equipment/equipment-create-2nd.html", {"equipment_name_form": equipment_name_form})

# special_model_formset = DrugFormset(request.POST or None, instance=equipment_name_form.instance)
# if request.method == "POST":
#     if equipment_name_form.is_valid() and special_model_formset.is_valid():
#         base = equipment_name_form.save()
#         special_model_formset.instance = base
#         special_model_formset.save()
# return render(request, "equipment/equipment-create-2nd.html", {"equipment_name_form": equipment_name_form,
#                                                                "special_model_formset": special_model_formset})

#

#
# child_model1_formset = ChildModel1Formset(request.POST or None, queryset=ChildModel1.objects.none())
