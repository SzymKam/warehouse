from __future__ import annotations
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
    CreateView,
)
from .models import Container
from .forms import ContainerForm, create_forms
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponse
from .constants import MEDICAL_EQUIPMENT_NAME_CHOICES
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


def warehouse_main(request):
    """render main warehouse page"""
    return render(
        request, "containers/warehouse-main.html", {"title": "Main Warehouse"}
    )


# views for containers
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

    def get_data_from_all_models(self, container_id):
        data = []
        for model in MODEL_LIST:
            query = model.objects.filter(container=container_id)
            data.append(query)
        return data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["equipment"] = self.get_data_from_all_models(
            container_id=self.object.id
        )
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


from .constants import DRUGS, FLUIDS


class EquipmentCreate:
    @staticmethod
    def get_name(request):
        if request.method == "POST":
            name = request.POST["name"]
            return redirect("test-object-create", name=name)
        return render(
            request,
            "equipment/equipment-create-1st.html",
            {"name_choices": MEDICAL_EQUIPMENT_NAME_CHOICES},
        )

    @staticmethod
    def select_object_to_create(request, name):
        forms = create_forms()
        initial = {"name": name}
        if name in dict(DRUGS).keys():
            form_obj = forms.get("DrugForm")
        elif name in dict(FLUIDS).keys():
            form_obj = forms.get("FluidForm")
        elif name == "Cannula":
            form_obj = forms.get("CannulaForm")
        elif name == "Needle":
            form_obj = forms.get("NeedleForm")
        elif name == "Syringe":
            form_obj = forms.get("SyringeForm")
        elif name == "BIG":
            form_obj = forms.get("BIGForm")
        elif name == "LT tube":
            form_obj = forms.get("LtTubeForm")
        elif name == "Gauze":
            form_obj = forms.get("GauzeForm")
        elif name == "Sterile gloves":
            form_obj = forms.get("SterileGlovesForm")
        elif name == "Gloves":
            form_obj = forms.get("GlovesForm")
        elif name == "NPA tube":
            form_obj = forms.get("NasopharyngealTubeForm")
        elif name == "OPA tube":
            form_obj = forms.get("OropharyngealTubeForm")
        elif name == "ET tube":
            form_obj = forms.get("EndotrachealTubeForm")
        elif name == "Laryngoscope blade":
            form_obj = forms.get("LaryngoscopeBladeForm")
        elif name == "Oxygen mask":
            form_obj = forms.get("OxygenMaskForm")
        elif name == "Ventilation mask":
            form_obj = forms.get("VentilationMaskForm")
        else:
            form_obj = forms.get("MedicalEquipmentForm")

        form = form_obj.form(request.POST or None, initial=initial)
        if form.is_valid() and request.method == "POST":
            form.save()
            messages.success(request, f"{name} created!")
            return redirect("containers-home")
        return render(request, "equipment/equipment-create-2nd.html", {"form": form})


from queryset_sequence import QuerySetSequence


class EquipmentRetrieve:
    @staticmethod
    def retrieve_equipment(request):
        queryset = []
        for model in MODEL_LIST:
            elements = model.objects.all()
            queryset.append(elements)
        query = QuerySetSequence(queryset)
        return render(
            request, "equipment/equipment-list.html", {"object_list": query._querysets}
        )


# class EquipmentUpdate:
# def update(request, element):


class EquipmentDelete:
    @staticmethod
    def delete_equipment(request, pk, name, container):
        if name in dict(DRUGS).keys():
            model_name = Drug
        elif name in dict(FLUIDS).keys():
            model_name = Fluid
        elif name == "Cannula":
            model_name = Cannula
        elif name == "Needle":
            model_name = Needle
        elif name == "Syringe":
            model_name = Syringe
        elif name == "BIG":
            model_name = BIG
        elif name == "LT tube":
            model_name = LtTube
        elif name == "Gauze":
            model_name = Gauze
        elif name == "Sterile gloves":
            model_name = SterileGloves
        elif name == "Gloves":
            model_name = Gloves
        elif name == "NPA tube":
            model_name = NasopharyngealTube
        elif name == "OPA tube":
            model_name = OropharyngealTube
        elif name == "ET tube":
            model_name = EndotrachealTube
        elif name == "Laryngoscope blade":
            model_name = LaryngoscopeBlade
        elif name == "Oxygen mask":
            model_name = OxygenMask
        elif name == "Ventilation mask":
            model_name = VentilationMask
        else:
            model_name = MedicalEquipment

        object_to_delete = get_object_or_404(klass=model_name, pk=pk)
        if request.method == "POST":
            object_to_delete.delete()
            messages.warning(request, f"{object_to_delete.name} deleted!")
            return redirect("containers-detail", pk=container)
        return render(
            request,
            "equipment/equipment-delete.html",
            {"name": name, "container": container},
        )
