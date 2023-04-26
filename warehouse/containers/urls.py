from django.urls import path
from .views import (
    ContainerDelete,
    ContainerUpdate,
    ContainerCreate,
    ContainerView,
    ContainerDetail,
    EquipmentCreate,
    EquipmentRetrieve,
    EquipmentDelete,
    EquipmentUpdate,
)
from .views import main_page


urlpatterns = [
    # main page
    path("", main_page, name="main-page"),
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
    # CRUD for temporary
    path(
        "temporary/create<int:container>",
        EquipmentCreate.get_name,
        name="temporary-create-1st",
    ),
    path(
        "temporary/create/<str:name>&<int:container>",
        EquipmentCreate.select_object_to_create,
        name="temporary-create-2nd",
    ),
    path(
        "temporary/delete/<int:pk>&<str:name>&<int:container>",
        EquipmentDelete.delete_equipment,
        name="temporary-delete",
    ),
    path("temporary/all/", EquipmentRetrieve.retrieve_equipment, name="temporary-all"),
    path(
        "temporary/update/<int:pk>&<str:name>&<int:container>",
        EquipmentUpdate.update_equipment,
        name="temporary-update",
    ),
]
