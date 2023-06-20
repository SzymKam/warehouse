from API.serializers.equipment_serializer import (
    MedicalEquipmentSerializer,
    DrugSerializer,
    FluidSerializer,
    CannulaSerializer,
    NeedleSerializer,
    SyringeSerializer,
    BIGSerializer,
    LtTubeSerializer,
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
