from django.views.generic import TemplateView
from django.urls import path
from rest_framework.schemas import get_schema_view
from rest_framework.routers import SimpleRouter

from API.views.containers_crud_API import ContainersViewSet
from API.views.equipment_crud_API import (
    EquipmentViewSet,
)
from API.views.all_models_viewset import (
    DrugViewset,
    MedicalEquipmentViewset,
    FluidViewset,
    CannulaViewset,
    NeedleViewset,
    SyringeViewset,
    BIGViewset,
    LtTubeViewset,
    GlovesViewset,
    SterileGlovesViewset,
    GauzeViewset,
    NasopharyngealTubeViewset,
    OropharyngealTubeViewset,
    EndotrachealTubeViewset,
    LaryngoscopeBladeViewset,
    OxygenMaskViewset,
    VentilationMaskViewset,
)
from .views.staff_crud_API import StaffViewSet


router = SimpleRouter()
router.register(r"staffs", StaffViewSet)
router.register(r"containers", ContainersViewSet)
router.register(r"equipment", EquipmentViewSet, basename="equipment")

router.register(r"drug", DrugViewset)
router.register(r"medical-equipment", MedicalEquipmentViewset)
router.register(r"fluid", FluidViewset)
router.register(r"cannula", CannulaViewset)
router.register(r"needle", NeedleViewset)
router.register(r"syringe", SyringeViewset)
router.register(r"big", BIGViewset)
router.register(r"lt-tube", LtTubeViewset)
router.register(r"gloves", GlovesViewset)
router.register(r"sterile-gloves", SterileGlovesViewset)
router.register(r"gauze", GauzeViewset)
router.register(r"npa-tube", NasopharyngealTubeViewset)
router.register(r"opa-tube", OropharyngealTubeViewset)
router.register(r"et-tube", EndotrachealTubeViewset)
router.register(r"laryngoscope-blade", LaryngoscopeBladeViewset)
router.register(r"oxygen-mask", OxygenMaskViewset)
router.register(r"ventilation-mask", VentilationMaskViewset)


urlpatterns = [
    path(
        "openapi",
        get_schema_view(
            title="Your Project", description="API for all things …", version="1.0.0"
        ),
        name="openapi-schema",
    ),
    path(
        "redoc/",
        TemplateView.as_view(
            template_name="API/redoc.html",
            extra_context={"schema_url": "openapi-schema"},
        ),
        name="redoc",
    ),
] + router.urls
