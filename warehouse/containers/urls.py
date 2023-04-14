from django.urls import path
from .views import (
    ContainerDelete,
    ContainerUpdate,
    ContainerCreate,
    ContainerView,
    ContainerDetail,
    # MedicalEquipmentCreate,
    MedicalEquipmentDelete,
    get_name,
    select_object_to_create,
    RetrieveMedicalEquipment,
)
from .views import warehouse_main


urlpatterns = [
    # main page
    path("", warehouse_main, name="warehouse-main"),
    # CRUD for containers
    path("containers/", ContainerView.as_view(), name="containers-home"),
    path("containers/<int:pk>", ContainerDetail.as_view(), name="containers-detail"),
    path(
        "containers/update/<int:pk>",
        ContainerUpdate.as_view(),
        name="containers-update",
    ),
    path("containers/create", ContainerCreate.as_view(), name="containers-create"),
    path(
        "containers/delete/<int:pk>",
        ContainerDelete.as_view(),
        name="containers-delete",
    ),
    # CRUD for equipment
    path("equipment/create", get_name, name="equipment-create"),
    path(
        "equipment/create<str:name>", select_object_to_create, name="test-object-create"
    ),
    path(
        "equipment/delete/<int:pk>",
        MedicalEquipmentDelete.as_view(),
        name="equipment-delete",
    ),
    path("equipment/all", RetrieveMedicalEquipment.as_view(), name="equipment-all"),
]
