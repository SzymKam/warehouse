from django.urls import path
from rest_framework.routers import SimpleRouter
from API.views.containers_crud_API import (
    GetAllContainers,
    GetContainer,
    CreateContainer,
    DeleteContainer,
    UpdateContainer,
)

# from API.views.staff_crud_API import (
#     GetAllStaff,
#     GetStaff,
#     CreateStaff,
#     DeleteStaff,
#     UpdateStaff,
# )
from API.views.equipment_crud_API import (
    GetAllEquipment,
    GetEquipment,
    DeleteEquipment,
    UpdateEquipment,
    CreateEquipment,
)

from .views.staff_crud_API import StaffViewSet

router = SimpleRouter()
router.register(r"staffs", StaffViewSet)

urlpatterns = [
    # containers crud
    path("containers/", GetAllContainers.as_view(), name="get-all-containers"),
    path("containers/<int:pk>/", GetContainer.as_view(), name="get-container"),
    path("containers/create/", CreateContainer.as_view(), name="create-container"),
    path(
        "containers/delete/<int:pk>/",
        DeleteContainer.as_view(),
        name="delete-container",
    ),
    path(
        "containers/update/<int:pk>/",
        UpdateContainer.as_view(),
        name="update-container",
    ),
    # equipment crud
    path("equipment/", GetAllEquipment.as_view(), name="get-all-equipment"),
    path("equipment/<int:pk>/", GetEquipment.as_view(), name="get-equipment"),
    path("equipment/create/", CreateEquipment.as_view(), name="create-equipment"),
    path(
        "equipment/delete/<int:pk>/", DeleteEquipment.as_view(), name="delete-equipment"
    ),
    path(
        "equipment/update/<int:pk>/", UpdateEquipment.as_view(), name="update-equipment"
    ),
] + router.urls
