from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Container


# class ContainerListView(ListView):
#     model = Container
#     template_name = "containers/containers-home.html"
#


class ContainerDetailView(DetailView):
    model = Container
    template_name = "containers/containers-detail.html"


def container_list(request):
    containers = Container.objects.all()
    return render(
        request,
        "containers/containers-home.html",
        {"title": "Containers", "containers": containers},
    )


def container_detail(request, id):
    container = Container.objects.filter(id=id)
    print(container)
    return render(
        request,
        "containers/containers-detail.html",
        {"title": "Container", "container": container},
    )
