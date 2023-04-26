from __future__ import annotations
from typing import Type, Optional
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
    CreateView,
)
from .constants import DRUGS, FLUIDS
from .models import Container
from .forms import ContainerForm, create_forms
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponse
from .constants import MEDICAL_EQUIPMENT_NAME_CHOICES
from queryset_sequence import QuerySetSequence
from django.forms import Form, BaseModelFormSet
from django.db.models import Model
from .models import (
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


def main_page(request):
    """main page of app"""
    return render(
        request,
        "containers/main-page.html",
        {"title": "GRM Main Page", "subtitle": "Dashboard"},
    )


def get_form_class_and_model_by_name(
    name: str, forms: Optional[dict[str, Type[BaseModelFormSet]]] = None
) -> tuple[Form, Model]:
    if forms is None:
        forms = {}

    name_to_form_class = {
        **{k: (forms.get("DrugForm"), Drug) for k in dict(DRUGS).keys()},
        **{k: (forms.get("FluidForm"), Fluid) for k in dict(FLUIDS).keys()},
        "Cannula": (forms.get("CannulaForm"), Cannula),
        "Needle": (forms.get("NeedleForm"), Needle),
        "Syringe": (forms.get("SyringeForm"), Syringe),
        "BIG": (forms.get("BIGForm"), BIG),
        "LT tube": (forms.get("LtTubeForm"), LtTube),
        "Gauze": (forms.get("Gauze"), Gauze),
        "Sterile gloves": (forms.get("SterileGlovesForm"), SterileGloves),
        "Gloves": (forms.get("SyringeForm"), Syringe),
        "NPA tube": (forms.get("SyringeForm"), NasopharyngealTube),
        "OPA tube": (forms.get("SyringeForm"), OropharyngealTube),
        "ET tube": (forms.get("SyringeForm"), EndotrachealTube),
        "Laryngoscope blade": (forms.get("SyringeForm"), LaryngoscopeBlade),
        "Oxygen mask": (forms.get("SyringeForm"), OxygenMask),
        "Ventilation mask": (forms.get("SyringeForm"), VentilationMask),
    }

    return name_to_form_class.get(
        name, (forms.get("MedicalEquipmentForm"), MedicalEquipment)
    )


class ContainerView(ListView):
    queryset = Container.objects.all()
    template_name = "containers/containers-list.html"

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "GRM Containers"
        context["subtitle"] = "Containers"
        return context


class ContainerDetail(DetailView):
    template_name = "containers/containers-detail.html"
    queryset = Container.objects.all()

    @staticmethod
    def get_data_from_all_models(container_id):
        data = []
        for model in MODEL_LIST:
            query = model.objects.filter(container=container_id)
            data.append(query)
        return data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["temporary"] = self.get_data_from_all_models(
            container_id=self.object.id
        )
        context["title"] = "GRM " + str(context["object"])
        context["subtitle"] = context["object"]
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "GRM update container"
        context["subtitle"] = "Updating container"
        return context


class ContainerCreate(CreateView):
    model = Container
    template_name = "containers/containers-create.html"
    form_class = ContainerForm
    success_url = reverse_lazy("containers-home")
    queryset = Container.objects.all()

    def form_valid(self, form):
        messages.success(self.request, "Container crated!")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["title"] = "GRM New container"
        context["subtitle"] = "Creating new container"
        return context


class ContainerDelete(DeleteView):
    template_name = "containers/containers-delete.html"
    model = Container
    success_url = reverse_lazy("containers-home")

    def form_valid(self, form):
        messages.warning(self.request, "Container deleted!")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "GRM container delete"
        context["subtitle"] = "Delete container"
        return context


class EquipmentCreate:
    @staticmethod
    def get_name(request, container):
        if request.method == "POST":
            name = request.POST["name"]
            return redirect("temporary-create-2nd", name=name, container=container)
        return render(
            request,
            "containers/temporary-create-1st.html",
            {
                "name_choices": MEDICAL_EQUIPMENT_NAME_CHOICES,
                "title": "GRM Create object",
                "subtitle": "Create new element",
            },
        )

    @staticmethod
    def select_object_to_create(request, name, container):
        initial = {"name": name, "container": Container.objects.get(pk=container)}

        form_obj, _ = get_form_class_and_model_by_name(name, create_forms())

        form = form_obj.form(request.POST or None, initial=initial)
        if form.is_valid() and request.method == "POST":
            form.save()
            messages.success(request, f"{name} created!")
            return redirect("containers-detail", pk=container)
        return render(
            request,
            "containers/temporary-create-2nd.html",
            {
                "form": form,
                "name": name,
                "title": "GRM Create object",
                "subtitle": f"Create new {name}",
            },
        )


class EquipmentRetrieve:
    @staticmethod
    def retrieve_equipment(request):
        queryset = []
        for model in MODEL_LIST:
            elements = model.objects.all()
            queryset.append(elements)
        query = QuerySetSequence(queryset)
        return render(
            request,
            "containers/temporary-all.html",
            {
                "object_list": query._querysets,
                "title": "GRM All temporary",
                "subtitle": "All temporary",
            },
        )


class EquipmentUpdate:
    @staticmethod
    def update_equipment(request, pk, name, container):
        form_obj, model_name = get_form_class_and_model_by_name(name, create_forms())
        object_to_update = get_object_or_404(klass=model_name, pk=pk)
        form = form_obj.form(request.POST or None, instance=object_to_update)
        if request.method == "POST" and form.is_valid():
            form.save()
            messages.info(request, f"{name} updated")
            return redirect("containers-detail", pk=container)
        return render(
            request,
            "containers/temporary-update.html",
            {
                "form": form,
                "name": name,
                "title": "GRM Equipment update",
                "subtitle": "Equipment update",
            },
        )


class EquipmentDelete:
    @staticmethod
    def delete_equipment(request, pk, name, container):
        _, model_name = get_form_class_and_model_by_name(name)
        object_to_delete = get_object_or_404(klass=model_name, pk=pk)
        if request.method == "POST":
            object_to_delete.delete()
            messages.warning(request, f"{object_to_delete.name} deleted!")
            return redirect("containers-detail", pk=container)
        return render(
            request,
            "containers/temporary-delete.html",
            {
                "name": name,
                "container": container,
                "title": "GRM Equipment delete",
                "subtitle": "Equipment delete",
            },
        )
