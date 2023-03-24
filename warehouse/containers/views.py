from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Container, MedicalEquipment
from .forms import ContainerForm


# class ContainerListView(ListView):
#     model = Container
#     template_name = "containers/containers-home.html"
#


# class ContainerDetailView(DetailView):
#     model = Container
#     template_name = "containers/containers-detail.html"
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
    container = Container.objects.filter(id=id)
    equipment = MedicalEquipment.objects.filter(container=id)
    name = container[0].name
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
            return redirect("containers-home")
    return render(request, "containers/containers-create.html", {"form": form})
