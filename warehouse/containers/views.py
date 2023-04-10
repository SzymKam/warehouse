from __future__ import annotations
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
    CreateView,
)
from .models import Container, BaseEquipment
from .forms import ContainerForm, MedicalEquipmentForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponse


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
    model = BaseEquipment
    queryset = BaseEquipment.objects.all()
    success_url = reverse_lazy("containers-home")
    form_class = MedicalEquipmentForm

    def form_valid(self, form):
        messages.success(self.request, "Equipment added")
        return super().form_valid(form)


class MedicalEquipmentDelete(DeleteView):
    model = BaseEquipment
    success_url = reverse_lazy("containers-home")
    template_name = "equipment/equipment-delete.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["container"] = self.object.container
        print(context["container"])
        return context


def create_or_edit(request):
    pass


#     equipment_name_form = MedicalEquipmentNameForm(request.POST)
#     if request.method == "POST":
#         name = request.POST.get("name")
#         match name:
#             case _:
#                 full_equipment_form = MedicalEquipmentForm(request.POST)
#                 # if request.method == "POST":
#                 # if full_equipment_form.is_valid():
#                 # #         # full_equipment_form.save()
#                 #         return HttpResponse(name)
#
#                 return render(request, "equipment/equipment-create-2nd.html", {"full_equipment_form": full_equipment_form})
#
#     return render(
#         request,
#         "equipment/equipment-create-2nd.html",
#         {"equipment_name_form": equipment_name_form},
#     )
#
#
#     # base_model_form = MedicalEquipmentForm(request.POST or None)
#     #
#
# child_formset = DrugFormset(request.POST or None, instance=base_model_form.instance)
#
# if request.method == "POST":
#     if base_model_form.is_valid() and child_formset.is_valid():
#         base_model = base_model_form.save()
#         child_formset.instance = base_model
#         child_formset.save()
#         messages.info(request, "Created")
#
# return render(
#     request,
#     "equipment/equipment-create-2nd.html",
#     {
#         "child_formset": child_formset,
#         "base_form": base_model_form,
#     },
# )
