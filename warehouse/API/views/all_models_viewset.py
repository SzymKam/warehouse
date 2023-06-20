from API.serializers.equipment_serializer import (
    MedicalEquipmentSerializer,
    DrugSerializer,
    FluidSerializer,
    CannulaSerializer,
    NeedleSerializer,
    SyringeSerializer,
    BIGSerializer,
    LtTubeSerializer,
    GlovesSerializer,
    SterileGlovesSerializer,
    GauzeSerializer,
    NasopharyngealTubeSerializer,
    OropharyngealTubeSerializer,
    EndotrachealTubeSerializer,
    LaryngoscopeBladeSerializer,
    OxygenMaskSerializer,
    VentilationMaskSerializer,
)
from containers.models import (
    Drug,
    MedicalEquipment,
    Fluid,
    Cannula,
    Needle,
    Syringe,
    BIG,
    LtTube,
    Gloves,
    SterileGloves,
    Gauze,
    NasopharyngealTube,
    OropharyngealTube,
    EndotrachealTube,
    LaryngoscopeBlade,
    OxygenMask,
    VentilationMask,
)
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    RetrieveModelMixin,
    ListModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
)
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions


class MedicalEquipmentViewset(
    RetrieveModelMixin,
    ListModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet,
):
    serializer_class = MedicalEquipmentSerializer
    queryset = MedicalEquipment.objects.all()
    permission_classes = [IsAuthenticated, DjangoModelPermissions]


class DrugViewset(
    RetrieveModelMixin,
    ListModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet,
):
    serializer_class = DrugSerializer
    queryset = Drug.objects.all()
    permission_classes = [IsAuthenticated, DjangoModelPermissions]


class FluidViewset(
    RetrieveModelMixin,
    ListModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet,
):
    serializer_class = FluidSerializer
    queryset = Fluid.objects.all()
    permission_classes = [IsAuthenticated, DjangoModelPermissions]


class CannulaViewset(
    RetrieveModelMixin,
    ListModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet,
):
    serializer_class = CannulaSerializer
    queryset = Cannula.objects.all()
    permission_classes = [IsAuthenticated, DjangoModelPermissions]


class NeedleViewset(
    RetrieveModelMixin,
    ListModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet,
):
    serializer_class = NeedleSerializer
    queryset = Needle.objects.all()
    permission_classes = [IsAuthenticated, DjangoModelPermissions]


class SyringeViewset(
    RetrieveModelMixin,
    ListModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet,
):
    serializer_class = SyringeSerializer
    queryset = Syringe.objects.all()
    permission_classes = [IsAuthenticated, DjangoModelPermissions]


class BIGViewset(
    RetrieveModelMixin,
    ListModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet,
):
    serializer_class = BIGSerializer
    queryset = BIG.objects.all()
    permission_classes = [IsAuthenticated, DjangoModelPermissions]


class LtTubeViewset(
    RetrieveModelMixin,
    ListModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet,
):
    serializer_class = LtTubeSerializer
    queryset = LtTube.objects.all()
    permission_classes = [IsAuthenticated, DjangoModelPermissions]


class GlovesViewset(
    RetrieveModelMixin,
    ListModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet,
):
    serializer_class = GlovesSerializer
    queryset = Gloves.objects.all()
    permission_classes = [IsAuthenticated, DjangoModelPermissions]


class SterileGlovesViewset(
    RetrieveModelMixin,
    ListModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet,
):
    serializer_class = SterileGlovesSerializer
    queryset = SterileGloves.objects.all()
    permission_classes = [IsAuthenticated, DjangoModelPermissions]


class GauzeViewset(
    RetrieveModelMixin,
    ListModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet,
):
    serializer_class = GauzeSerializer
    queryset = Gauze.objects.all()
    permission_classes = [IsAuthenticated, DjangoModelPermissions]


class NasopharyngealTubeViewset(
    RetrieveModelMixin,
    ListModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet,
):
    serializer_class = NasopharyngealTubeSerializer
    queryset = NasopharyngealTube.objects.all()
    permission_classes = [IsAuthenticated, DjangoModelPermissions]


class OropharyngealTubeViewset(
    RetrieveModelMixin,
    ListModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet,
):
    serializer_class = OropharyngealTubeSerializer
    queryset = OropharyngealTube.objects.all()
    permission_classes = [IsAuthenticated, DjangoModelPermissions]


class EndotrachealTubeViewset(
    RetrieveModelMixin,
    ListModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet,
):
    serializer_class = EndotrachealTubeSerializer
    queryset = EndotrachealTube.objects.all()
    permission_classes = [IsAuthenticated, DjangoModelPermissions]


class LaryngoscopeBladeViewset(
    RetrieveModelMixin,
    ListModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet,
):
    serializer_class = LaryngoscopeBladeSerializer
    queryset = LaryngoscopeBlade.objects.all()
    permission_classes = [IsAuthenticated, DjangoModelPermissions]


class OxygenMaskViewset(
    RetrieveModelMixin,
    ListModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet,
):
    serializer_class = OxygenMaskSerializer
    queryset = OxygenMask.objects.all()
    permission_classes = [IsAuthenticated, DjangoModelPermissions]


class VentilationMaskViewset(
    RetrieveModelMixin,
    ListModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet,
):
    serializer_class = VentilationMaskSerializer
    queryset = VentilationMask.objects.all()
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
