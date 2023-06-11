from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView,
)
from API.serializers.equipment_serializer import EquipmentSerializer
from rest_framework.permissions import IsAuthenticated
from containers.models import MedicalEquipment


class GetAllEquipment(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EquipmentSerializer
    queryset = MedicalEquipment.objects.all()


class GetEquipment(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EquipmentSerializer
    queryset = MedicalEquipment


class CreateEquipment(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EquipmentSerializer


class UpdateEquipment(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EquipmentSerializer
    queryset = MedicalEquipment


class DeleteEquipment(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EquipmentSerializer
    queryset = MedicalEquipment
