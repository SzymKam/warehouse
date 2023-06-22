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
from rest_framework.exceptions import ValidationError
from API.constants import name_to_serializer


def validate_name_for_update(serializer):
    if "name" in serializer.validated_data.keys():
        if serializer.validated_data["name"] not in name_to_serializer().keys():
            raise ValidationError("Invalid name")


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

    def perform_update(self, serializer):
        validate_name_for_update(serializer)
        super().perform_update(serializer)


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

    def perform_update(self, serializer):
        validate_name_for_update(serializer)
        super().perform_update(serializer)


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

    def perform_update(self, serializer):
        validate_name_for_update(serializer)
        super().perform_update(serializer)


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
