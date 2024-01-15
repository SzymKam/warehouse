from __future__ import annotations
from typing import Any
from django.views.generic import (
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
    CreateView,
)
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from containers.models import (
    MedicalEquipment,
    Drug,
    Fluid,
    Cannula,
    Needle,
    Syringe,
    BIG,
    LtTube,
    Gloves,
    SterileGloves,
    Gauze,
    NasopharyngealTube,
    OropharyngealTube,
    EndotrachealTube,
    LaryngoscopeBlade,
    OxygenMask,
    VentilationMask,
)

from ..forms import ContainerForm
from ..models import Container

MODEL_LIST = [
    MedicalEquipment,
    Drug,
    Fluid,
    Cannula,
    Needle,
    Syringe,
    BIG,
    LtTube,
    Gloves,
    SterileGloves,
    Gauze,
    NasopharyngealTube,
    OropharyngealTube,
    EndotrachealTube,
    LaryngoscopeBlade,
    OxygenMask,
    VentilationMask,
]


class ContainerView(LoginRequiredMixin, ListView):
    template_name = "containers/containers-list.html"
    queryset = Container.objects.all()

    def get(self, request, *args, **kwargs) -> Any:
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "GRM Containers"
        context["subtitle"] = "Containers"
        context["main"] = Container.get_main_container().id
        return context


class ContainerDetail(LoginRequiredMixin, DetailView):
    template_name = "containers/containers-detail.html"
    queryset = Container.objects.all()

    @staticmethod
    def get_data_from_all_models(container_id: int) -> list[Any]:
        data = []
        for model in MODEL_LIST:
            query = model.objects.filter(container=container_id)
            data.append(query)
        return data

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["equipment"] = self.get_data_from_all_models(
            container_id=self.object.id
        )
        context["title"] = "GRM " + str(context["object"])
        context["subtitle"] = context["object"]
        return context


class ContainerUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = "containers.change_container"
    permission_denied_message = "Only medical magazine admins can update containers"
    login_url = "main-page"
    model = Container
    template_name = "containers/containers-update.html"
    form_class = ContainerForm

    def get_success_url(self):
        return reverse_lazy("containers-detail", args=(self.object.id,))

    def form_valid(self, form):
        messages.info(self.request, "Container updated!")
        return super().form_valid(form)

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "GRM update container"
        context["subtitle"] = "Updating container"
        return context


class ContainerCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ("containers.add_container",)
    permission_denied_message = "Only medical magazine admins can add containers"
    login_url = "main-page"
    model = Container
    template_name = "containers/containers-create.html"
    form_class = ContainerForm
    success_url = reverse_lazy("containers-home")
    queryset = Container.objects.all()

    def form_valid(self, form):
        messages.success(self.request, "Container created!")
        return super().form_valid(form)

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data()
        context["title"] = "GRM New container"
        context["subtitle"] = "Creating new container"
        return context


class ContainerDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = "containers.delete_container"
    permission_denied_message = "Only medical magazine admins can delete containers"
    template_name = "containers/containers-delete.html"
    model = Container
    success_url = reverse_lazy("containers-home")

    def form_valid(self, form):
        messages.warning(self.request, "Container deleted!")
        return super().form_valid(form)

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "GRM container delete"
        context["subtitle"] = "Delete container"
        return context
