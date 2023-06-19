from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView,
)
from rest_framework.response import Response
from API.serializers.equipment_serializer import (
    AllEquipmentSerializer,
    MedicalEquipmentSerializer,
)
from rest_framework.permissions import IsAuthenticated
from containers.models import MedicalEquipment, Drug
from API.constants import name_to_serializer
from rest_framework.viewsets import GenericViewSet
from rest_framework.exceptions import ValidationError
from rest_framework.mixins import (
    CreateModelMixin,
    RetrieveModelMixin,
    ListModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
)


class EquipmentViewSet(GenericViewSet, CreateModelMixin):
    permission_classes = [IsAuthenticated]
    serializer_class = AllEquipmentSerializer
    queryset = None

    def list(self, request):
        serializer = AllEquipmentSerializer(instance={}, many=False)
        return Response(serializer.data)


class GetEquipment(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AllEquipmentSerializer
    queryset = MedicalEquipment


class CreateEquipment(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MedicalEquipmentSerializer

    @staticmethod
    def get_class_serializer(name_value):
        serializer_dict = name_to_serializer()
        try:
            serializer = serializer_dict[name_value]
        except KeyError:
            raise ValidationError("Invalid name")
        return serializer

    def get_serializer(self, *args, **kwargs):
        name_value = self.request.data["name"]
        serializer_class = self.get_class_serializer(name_value)
        kwargs.setdefault("context", self.get_serializer_context())
        return serializer_class(*args, **kwargs)


class UpdateEquipment(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AllEquipmentSerializer
    queryset = MedicalEquipment


class DeleteEquipment(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AllEquipmentSerializer
    queryset = MedicalEquipment
