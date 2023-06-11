from django.urls import path
from API.views.containers_crud_API import (
    GetAllContainers,
    GetContainer,
    CreateContainer,
    DeleteContainer,
    UpdateContainer,
)
from API.views.staff_crud_API import (
    GetAllStaff,
    GetStaff,
    CreateStaff,
    DeleteStaff,
    UpdateStaff,
)
from API.views.equipment_crud_API import (
    GetAllEquipment,
    GetEquipment,
    DeleteEquipment,
    UpdateEquipment,
    CreateEquipment,
)


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
    # staff crud
    path("staff/", GetAllStaff.as_view(), name="get-all-staff"),
    path("staff/<int:pk>/", GetStaff.as_view(), name="get-staff"),
    path("staff/create/", CreateStaff.as_view(), name="create-staff"),
    path("staff/delete/<int:pk>/", DeleteStaff.as_view(), name="delete-staff"),
    path("staff/update/<int:pk>/", UpdateStaff.as_view(), name="update-staff"),
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
]
