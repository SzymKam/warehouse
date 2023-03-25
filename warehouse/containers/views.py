from typing import Type
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
    CreateView,
)
from .models import Container, MedicalEquipment
from .forms import ContainerForm
from django.contrib import messages


def warehouse_main(request):
    """render main warehouse page"""
    return render(
        request, "containers/warehouse-main.html", {"title": "Main Warehouse"}
    )


def container_list(request):
    """render list of containers"""
    containers = Container.objects.all()
    return render(
        request,
        "containers/containers-home.html",
        {"title": "Containers", "containers": containers},
    )


def container_detail(request, id):
    """render detail about container by its id"""
    container = get_object_or_404(Container, id=id)
    equipment = MedicalEquipment.objects.filter(container=id)
    name = container.name
    return render(
        request,
        "containers/containers-detail.html",
        {"title": name, "container": container, "equipment": equipment},
    )


def container_create(request):
    """create new container"""
    form = ContainerForm()
    if request.method == "POST":
        form = ContainerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Created container!")
            return redirect("containers-home")
    return render(request, "containers/containers-create.html", {"form": form})


def container_delete(request, id):
    """delete container"""
    container = get_object_or_404(Container, id=id)
    if request.method == "POST":
        container.delete()
        return redirect("containers-home")
    return render(
        request, "containers/containers-delete.html", {"container": container}
    )


def container_update(request, id):
    """update container"""
    container = get_object_or_404(Container, id=id)
    form = ContainerForm(request.POST or None, instance=container)
    if form.is_valid():
        form.save()
        return redirect("containers-detail", id=id)
    return render(request, "containers/containers-update.html", {"form": form})


# class ContainerDelete(DeleteView):
#     template_name = 'containers/containers-delete.html'
#     success_url = "containers-home"
#     model = Container
