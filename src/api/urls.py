from django.views.generic import TemplateView
from django.urls import path
from rest_framework.schemas import get_schema_view
from rest_framework.routers import SimpleRouter

from api.views.containers_crud import ContainersViewSet
from api.views.equipment_crud import (
    EquipmentViewSet,
)
from api.views.all_models_viewset import (
    DrugViewSet,
    MedicalEquipmentViewSet,
    FluidViewSet,
    CannulaViewSet,
    NeedleViewSet,
    SyringeViewSet,
    BIGViewSet,
    LtTubeViewSet,
    GlovesViewSet,
    SterileGlovesViewSet,
    GauzeViewSet,
    NasopharyngealTubeViewSet,
    OropharyngealTubeViewSet,
    EndotrachealTubeViewSet,
    LaryngoscopeBladeViewSet,
    OxygenMaskViewSet,
    VentilationMaskViewSet,
)
from .views.staff_crud import StaffViewSet


router = SimpleRouter()
router.register(r"staffs", StaffViewSet)
router.register(r"containers", ContainersViewSet)
router.register(r"equipment", EquipmentViewSet, basename="equipment")

router.register(r"drug", DrugViewSet)
router.register(r"medical-equipment", MedicalEquipmentViewSet)
router.register(r"fluid", FluidViewSet)
router.register(r"cannula", CannulaViewSet)
router.register(r"needle", NeedleViewSet)
router.register(r"syringe", SyringeViewSet)
router.register(r"big", BIGViewSet)
router.register(r"lt-tube", LtTubeViewSet)
router.register(r"gloves", GlovesViewSet)
router.register(r"sterile-gloves", SterileGlovesViewSet)
router.register(r"gauze", GauzeViewSet)
router.register(r"npa-tube", NasopharyngealTubeViewSet)
router.register(r"opa-tube", OropharyngealTubeViewSet)
router.register(r"et-tube", EndotrachealTubeViewSet)
router.register(r"laryngoscope-blade", LaryngoscopeBladeViewSet)
router.register(r"oxygen-mask", OxygenMaskViewSet)
router.register(r"ventilation-mask", VentilationMaskViewSet)


urlpatterns = [
    path(
        "openapi",
        get_schema_view(
            title="Your Project", description="api for all things …", version="1.0.0"
        ),
        name="openapi-schema",
    ),
    path(
        "redoc/",
        TemplateView.as_view(
            template_name="api/redoc.html",
            extra_context={"schema_url": "openapi-schema"},
        ),
        name="redoc",
    ),
] + router.urls
