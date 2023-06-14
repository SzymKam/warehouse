from django.urls import path
from rest_framework.routers import SimpleRouter
from API.views.containers_crud_API import ContainersViewSet
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
router.register(r"containers", ContainersViewSet)


urlpatterns = [
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
