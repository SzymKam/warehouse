from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView,
)
from API.serializers.equipment_serializer import AllEquipmentSerializer
from rest_framework.permissions import IsAuthenticated
from containers.models import MedicalEquipment, Drug


class GetAllEquipment(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AllEquipmentSerializer
    queryset = Drug.objects.all()


class GetEquipment(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AllEquipmentSerializer
    queryset = MedicalEquipment


class CreateEquipment(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AllEquipmentSerializer
    # ?= tube
    # def get_serializer_class(self):
    #     value = self.kwargs.get('value')
    #     if value == 'tube':
    #         return TubeSerializer

    # def get(self):
    #     serializer_class = self.get_serializer_class()
    #     serializer = serializer_class(data=request.data)


class UpdateEquipment(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AllEquipmentSerializer
    queryset = MedicalEquipment


class DeleteEquipment(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AllEquipmentSerializer
    queryset = MedicalEquipment
