from rest_framework.routers import SimpleRouter
from API.views.containers_crud_API import ContainersViewSet
from API.views.equipment_crud_API import (
    EquipmentViewSet,
)
from .views.staff_crud_API import StaffViewSet
from API.views.all_models_viewset import (
    DrugViewset,
    MedicalEquipmentViewset,
    FluidViewset,
    CannulaViewset,
    NeedleViewset,
    SyringeViewset,
    BIGViewset,
    LtTubeViewset,
)

router = SimpleRouter()
router.register(r"staffs", StaffViewSet)
router.register(r"containers", ContainersViewSet)
router.register(r"equipment", EquipmentViewSet, basename="equipment")

router.register(r"drug", DrugViewset)
router.register(r"medical_equipment", MedicalEquipmentViewset)
router.register(r"fluid", FluidViewset)
router.register(r"cannula", CannulaViewset)
router.register(r"needle", NeedleViewset)
router.register(r"syringe", SyringeViewset)
router.register(r"big", BIGViewset)
router.register(r"lt-tube", LtTubeViewset)


urlpatterns = [] + router.urls
