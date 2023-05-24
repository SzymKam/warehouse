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
    save_to_pdf,
)
from .views import main_page
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # main page
    path("", main_page, name="main-page"),
    # CRUD for containers
    path(
        "containers/", login_required(ContainerView.as_view()), name="containers-home"
    ),
    path(
        "containers/<int:pk>",
        login_required(ContainerDetail.as_view()),
        name="containers-detail",
    ),
    path(
        "containers/update/<int:pk>",
        login_required(ContainerUpdate.as_view()),
        name="containers-update",
    ),
    path(
        "containers/create",
        login_required(ContainerCreate.as_view()),
        name="containers-create",
    ),
    path(
        "containers/delete/<int:pk>",
        login_required(ContainerDelete.as_view()),
        name="containers-delete",
    ),
    # CRUD for temporary
    path(
        "equipment/create<int:container>",
        login_required(EquipmentCreate.get_name),
        name="equipment-create-1st",
    ),
    path(
        "equipment/create/<str:name>&<int:container>",
        login_required(EquipmentCreate.select_object_to_create),
        name="equipment-create-2nd",
    ),
    path(
        "equipment/delete/<int:pk>&<str:name>&<int:container>",
        login_required(EquipmentDelete.delete_equipment),
        name="equipment-delete",
    ),
    path(
        "equipment/all/",
        login_required(EquipmentRetrieve.retrieve_equipment),
        name="equipment-all",
    ),
    path(
        "equipment/update/<int:pk>&<str:name>&<int:container>",
        login_required(EquipmentUpdate.update_equipment),
        name="equipment-update",
    ),
    path("save_pdf/<str:element>/<slug:element_id>", save_to_pdf, name="save-pdf"),
    path("save_pdf/<str:element>/", save_to_pdf, name="save-pdf-no-id"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
