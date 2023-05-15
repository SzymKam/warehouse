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
from django.contrib.auth.decorators import login_required, permission_required
from .constants import MEDICAL_EQUIPMENT_NAME_CHOICES
from queryset_sequence import QuerySetSequence
from django.forms import Form, BaseModelFormSet
from django.db.models import Model
from django.contrib.auth.mixins import PermissionRequiredMixin
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


def error_403(request, exception):
    return render(request, "containers/403.html")


@login_required()
def main_page(request):
    """main page of app"""
    return render(
        request,
        "containers/main-page.html",
        {"title": "GRM Main Page", "subtitle": "Main page"},
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
        context["equipment"] = self.get_data_from_all_models(
            container_id=self.object.id
        )
        context["title"] = "GRM " + str(context["object"])
        context["subtitle"] = context["object"]
        return context


class ContainerUpdate(PermissionRequiredMixin, UpdateView):
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "GRM update container"
        context["subtitle"] = "Updating container"
        return context


class ContainerCreate(PermissionRequiredMixin, CreateView):
    permission_required = ("containers.add_container",)
    permission_denied_message = "Only medical magazine admins can add containers"
    login_url = "main-page"
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


class ContainerDelete(PermissionRequiredMixin, DeleteView):
    permission_required = "containers.delete_container"
    permission_denied_message = "Only medical magazine admins can delete containers"
    login_url = "main-page"
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


from django.shortcuts import render, HttpResponse
from django.template.loader import get_template, render_to_string
from xhtml2pdf import pisa


def save_to_pdf(request):
    # map_items = {
    #     'staff': Staff,
    #     'containers': Container,
    #
    # }
    # template_path = "containers/containers-list-for-render.html"
    # template = get_template(template_path)
    context = {"object_list": Container.objects.all()}
    # html = template.render(context)
    html = render_to_string(
        "containers/containers-list-for-render.html", context=context
    )
    # html = f"{template_path, context}"

    response = HttpResponse(content_type="")
    response["Content-Disposition"] = 'attachment; filename="my_pdf.pdf"'
    pdf = pisa.CreatePDF(html, dest=response)
    print(response)
    if pdf.err:
        return HttpResponse("Error while creating PDF: %s" % pdf.err)
    return response
