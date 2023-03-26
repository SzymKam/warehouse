from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
    CreateView,
)
from .models import Container, MedicalEquipment
from .forms import ContainerForm, MedicalEquipmentForm, DrugFormset
from django.contrib import messages
from django.urls import reverse_lazy


def warehouse_main(request):
    """render main warehouse page"""
    return render(
        request, "containers/warehouse-main.html", {"title": "Main Warehouse"}
    )


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


class BaseContainer:
    model = Container
    success_url = reverse_lazy("containers-home")


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


# def create_or_edit(request):
#     base_model_form = MedicalEquipmentForm(request.POST or None)
#     child_formset = DrugFormset(request.POST or None, instance=base_model_form.instance)
#
#     if request.method == 'POST':
#         print('post')
#         if base_model_form.is_valid() and child_formset.is_valid():
#             base_model = base_model_form.save()
#             print('adult')
#             child_formset.instance = base_model
#             child_formset.save()
#             print('saved')
#             messages.info(request, 'Created')
#         else:
#             print('invalid')
#             print(base_model_form.errors)
#             print(child_formset.errors)
#
#     return render(request, 'equipment/equipment-create.html', {
#         'child_formset': child_formset,
#         'base_form': base_model_form,
#     })
