from rest_framework.response import Response
from api.serializers.equipment_serializer import (
    AllEquipmentSerializer,
)
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from api.constants import name_to_serializer
from rest_framework.viewsets import GenericViewSet
from rest_framework.exceptions import ValidationError
from rest_framework.mixins import CreateModelMixin
from containers.models import MedicalEquipment
from typing import Any


class EquipmentViewSet(GenericViewSet, CreateModelMixin):
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    serializer_class = AllEquipmentSerializer
    queryset = MedicalEquipment.objects.all()

    def list(self, request) -> Any:
        serializer = AllEquipmentSerializer(instance={}, many=False)
        return Response(serializer.data)

    @staticmethod
    def get_class_serializer(name_value: str) -> Any:
        serializer_dict = name_to_serializer()
        try:
            serializer = serializer_dict[name_value]
        except KeyError:
            raise ValidationError("Invalid name")
        return serializer

    def get_serializer(self, *args, **kwargs):
        name_value = self.request.data.get("name")
        serializer_class = self.get_class_serializer(name_value=name_value)
        kwargs.setdefault("context", self.get_serializer_context())
        return serializer_class(*args, **kwargs)
