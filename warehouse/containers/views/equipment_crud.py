from typing import Type, Optional
from django.shortcuts import render, redirect, get_object_or_404
from containers.constants import DRUGS, FLUIDS
from containers.models import Container
from containers.forms import create_forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from containers.constants import MEDICAL_EQUIPMENT_NAME_CHOICES
from queryset_sequence import QuerySetSequence
from django.forms import Form, BaseModelFormSet
from django.db.models import Model
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
        "Gauze": (forms.get("GauzeForm"), Gauze),
        "Sterile gloves": (forms.get("SterileGlovesForm"), SterileGloves),
        "Gloves": (forms.get("GlovesForm"), Gloves),
        "NPA tube": (forms.get("NasopharyngealTubeForm"), NasopharyngealTube),
        "OPA tube": (forms.get("OropharyngealTubeForm"), OropharyngealTube),
        "ET tube": (forms.get("EndotrachealTubeForm"), EndotrachealTube),
        "Laryngoscope blade": (forms.get("LaryngoscopeBladeForm"), LaryngoscopeBlade),
        "Oxygen mask": (forms.get("OxygenMaskForm"), OxygenMask),
        "Ventilation mask": (forms.get("VentilationMaskForm"), VentilationMask),
    }

    return name_to_form_class.get(
        name, (forms.get("MedicalEquipmentForm"), MedicalEquipment)
    )


class EquipmentCreate:
    @staticmethod
    @login_required()
    @permission_required("containers.add_drug", raise_exception=True)
    def get_name(request, container):
        if request.method == "POST":
            name = request.POST["name"]
            return redirect("equipment-create-2nd", name=name, container=container)
        return render(
            request,
            "containers/equipment-create-1st.html",
            {
                "name_choices": MEDICAL_EQUIPMENT_NAME_CHOICES,
                "title": "GRM Create object",
                "subtitle": "Create new element",
            },
        )

    @staticmethod
    @login_required()
    @permission_required("containers.add_drug", login_url="main-page")
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
            "containers/equipment-create-2nd.html",
            {
                "form": form,
                "name": name,
                "title": "GRM Create object",
                "subtitle": f"Create new {name}",
            },
        )


class EquipmentRetrieve:
    @staticmethod
    @login_required()
    def retrieve_equipment(request):
        queryset = []
        for model in MODEL_LIST:
            elements = model.objects.all()
            queryset.append(elements)
        query = QuerySetSequence(queryset)
        return render(
            request,
            "containers/equipment-all.html",
            {
                "object_list": query._querysets,
                "title": "GRM All equipment",
                "subtitle": "All equipment",
            },
        )


class EquipmentUpdate:
    @staticmethod
    @login_required()
    @permission_required("containers.change_drug", login_url="main-page")
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
            "containers/equipment-update.html",
            {
                "form": form,
                "name": name,
                "title": "GRM Equipment update",
                "subtitle": "Equipment update",
            },
        )


class EquipmentDelete:
    @staticmethod
    @login_required()
    @permission_required("containers.delete_drug", login_url="main-page")
    def delete_equipment(request, pk, name, container):
        _, model_name = get_form_class_and_model_by_name(name)
        object_to_delete = get_object_or_404(klass=model_name, pk=pk)
        if request.method == "POST":
            object_to_delete.delete()
            messages.warning(request, f"{object_to_delete.name} deleted!")
            return redirect("containers-detail", pk=container)
        return render(
            request,
            "containers/equipment-delete.html",
            {
                "name": name,
                "container": container,
                "title": "GRM Equipment delete",
                "subtitle": "Equipment delete",
            },
        )
