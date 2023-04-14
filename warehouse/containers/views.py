from __future__ import annotations
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
    CreateView,
)
from .models import Container, MedicalEquipment, BaseMedicalEquipment
from .forms import ContainerForm, create_forms, MedicalEquipmentForm, DrugForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponse
from .constants import MEDICAL_EQUIPMENT_NAME_CHOICES


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


# views for medical equipment
class MedicalEquipmentDelete(DeleteView):
    model = MedicalEquipment
    success_url = reverse_lazy("containers-home")
    template_name = "equipment/equipment-delete.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["container"] = self.object.container
        print(context["container"])
        return context


class RetrieveMedicalEquipment(ListView):
    queryset = BaseMedicalEquipment
    template_name = "equipment/equipment-list.html"


def get_name(request):
    if request.method == "POST":
        name = request.POST["name"]
        return redirect("test-object-create", name=name)
    return render(
        request,
        "equipment/equipment-create-1st.html",
        {"name_choices": MEDICAL_EQUIPMENT_NAME_CHOICES},
    )


from .constants import DRUGS, FLUIDS


def select_object_to_create(request, name):
    forms = create_forms()
    print(forms)
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
