from django.urls import path, include
from .views import DeleteView
from .views import (
    container_list,
    container_detail,
    warehouse_main,
    container_create,
    container_update,
    container_delete,
)


urlpatterns = [
    # path('', ContainerListView.as_view(), name='containers-home'),
    # path('<int:pk>/', ContainerDetailView.as_view(), name='containers-detail'),
    path("", warehouse_main, name="warehouse-main"),
    path("containers/", container_list, name="containers-home"),
    path("containers/<int:id>", container_detail, name="containers-detail"),
    path("containers/create", container_create, name="containers-create"),
    path("containers/delete/<int:id>", container_delete, name="containers-delete"),
    path("containers/update/<int:id>", container_update, name="containers-update"),
]
