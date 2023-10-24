from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from containers.views.container_crud import (
    ContainerView,
    ContainerDetail,
    ContainerUpdate,
    ContainerCreate,
    ContainerDelete,
)
from containers.views.equipment_crud import (
    EquipmentCreate,
    EquipmentDelete,
    EquipmentRetrieve,
    EquipmentUpdate,
)
from containers.views.pdf_save import save_to_pdf
from containers.views.equipment_standard import StandardEquipment
from containers.views.main_page import main_page

urlpatterns = (
    [
        # main page
        path("", main_page, name="main-page"),
        # CRUD for containers
        path("containers/", ContainerView.as_view(), name="containers-home"),
        path(
            "containers/<int:pk>",
            ContainerDetail.as_view(),
            name="containers-detail",
        ),
        path(
            "containers/update/<int:pk>",
            ContainerUpdate.as_view(),
            name="containers-update",
        ),
        path(
            "containers/create",
            ContainerCreate.as_view(),
            name="containers-create",
        ),
        path(
            "containers/delete/<int:pk>",
            ContainerDelete.as_view(),
            name="containers-delete",
        ),
        path(
            "equipment/create<int:container>",
            EquipmentCreate.get_name,
            name="equipment-create-1st",
        ),
        path(
            "equipment/create/<str:name>&<int:container>",
            EquipmentCreate.select_object_to_create,
            name="equipment-create-2nd",
        ),
        path(
            "equipment/delete/<int:pk>&<str:name>&<int:container>",
            EquipmentDelete.delete_equipment,
            name="equipment-delete",
        ),
        path(
            "equipment/all/",
            EquipmentRetrieve.retrieve_equipment,
            name="equipment-all",
        ),
        path(
            "equipment/update/<int:pk>&<str:name>&<int:container>",
            EquipmentUpdate.update_equipment,
            name="equipment-update",
        ),
        path("save_pdf/<str:element>/<slug:element_id>", save_to_pdf, name="save-pdf"),
        path("save_pdf/<str:element>/", save_to_pdf, name="save-pdf-no-id"),
        path(
            "equipment/standard/R1-backpack/",
            StandardEquipment.r1_backpack_standard,
            name="r1-backpack-standard",
        ),
        path(
            "equipment/standard/R1-additions/",
            StandardEquipment.r1_additions_standard,
            name="r1-additions-standard",
        ),
        path(
            "equipment/standard/ALS-backpack/",
            StandardEquipment.als_backpack_standard,
            name="als-backpack-standard",
        ),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
