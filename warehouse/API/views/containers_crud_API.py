from rest_framework.response import Response

from API.serializers.containers_serializer import (
    ContainerSerializer,
    DetailContainerSerializer,
)
from containers.models import Container
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.mixins import (
    CreateModelMixin,
    RetrieveModelMixin,
    ListModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
)
from rest_framework.viewsets import GenericViewSet
from API.constants import API_NAME_CHOICES
from rest_framework.exceptions import ValidationError


class ContainersViewSet(
    ListModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    RetrieveModelMixin,
    GenericViewSet,
):
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    serializer_class = ContainerSerializer
    queryset = Container.objects.all()

    def perform_create(self, serializer):
        name = serializer.validated_data.get("name")
        allowed_name = API_NAME_CHOICES
        if name not in allowed_name:
            raise ValidationError("Invalid name")
        serializer.save()

    def perform_update(self, serializer):
        name = serializer.validated_data.get("name")
        allowed_name = API_NAME_CHOICES
        if name not in allowed_name:
            raise ValidationError("Invalid name")
        serializer.save()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = DetailContainerSerializer(instance)
        return Response(serializer.data)
