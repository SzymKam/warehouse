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
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.exceptions import ValidationError
from API.constants import name_to_serializer


class EquipmentViewSetMixin(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def perform_update(self, serializer):
        EquipmentViewSetMixin.validate_name_for_update(serializer)
        super().perform_update(serializer)

    @staticmethod
    def validate_name_for_update(serializer):
        if "name" in serializer.validated_data.keys():
            if serializer.validated_data["name"] not in name_to_serializer().keys():
                raise ValidationError("Invalid name")


class MedicalEquipmentViewset(EquipmentViewSetMixin):
    serializer_class = MedicalEquipmentSerializer
    queryset = MedicalEquipment.objects.all()


class DrugViewset(EquipmentViewSetMixin):
    serializer_class = DrugSerializer
    queryset = Drug.objects.all()


class FluidViewset(EquipmentViewSetMixin):
    serializer_class = FluidSerializer
    queryset = Fluid.objects.all()


class CannulaViewset(EquipmentViewSetMixin):
    serializer_class = CannulaSerializer
    queryset = Cannula.objects.all()


class NeedleViewset(EquipmentViewSetMixin):
    serializer_class = NeedleSerializer
    queryset = Needle.objects.all()


class SyringeViewset(EquipmentViewSetMixin):
    serializer_class = SyringeSerializer
    queryset = Syringe.objects.all()


class BIGViewset(EquipmentViewSetMixin):
    serializer_class = BIGSerializer
    queryset = BIG.objects.all()


class LtTubeViewset(EquipmentViewSetMixin):
    serializer_class = LtTubeSerializer
    queryset = LtTube.objects.all()


class GlovesViewset(EquipmentViewSetMixin):
    serializer_class = GlovesSerializer
    queryset = Gloves.objects.all()


class SterileGlovesViewset(EquipmentViewSetMixin):
    serializer_class = SterileGlovesSerializer
    queryset = SterileGloves.objects.all()


class GauzeViewset(EquipmentViewSetMixin):
    serializer_class = GauzeSerializer
    queryset = Gauze.objects.all()


class NasopharyngealTubeViewset(EquipmentViewSetMixin):
    serializer_class = NasopharyngealTubeSerializer
    queryset = NasopharyngealTube.objects.all()


class OropharyngealTubeViewset(EquipmentViewSetMixin):
    serializer_class = OropharyngealTubeSerializer
    queryset = OropharyngealTube.objects.all()


class EndotrachealTubeViewset(EquipmentViewSetMixin):
    serializer_class = EndotrachealTubeSerializer
    queryset = EndotrachealTube.objects.all()


class LaryngoscopeBladeViewset(EquipmentViewSetMixin):
    serializer_class = LaryngoscopeBladeSerializer
    queryset = LaryngoscopeBlade.objects.all()


class OxygenMaskViewset(EquipmentViewSetMixin):
    serializer_class = OxygenMaskSerializer
    queryset = OxygenMask.objects.all()


class VentilationMaskViewset(EquipmentViewSetMixin):
    serializer_class = VentilationMaskSerializer
    queryset = VentilationMask.objects.all()
