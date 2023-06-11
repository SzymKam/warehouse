from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView,
)
from API.serializers.containers_serializer import ContainerSerializer
from containers.models import Container
from rest_framework.permissions import IsAuthenticated


class GetAllContainers(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ContainerSerializer
    queryset = Container.objects.all()


class GetContainer(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ContainerSerializer
    queryset = Container


class CreateContainer(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ContainerSerializer


class UpdateContainer(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ContainerSerializer
    queryset = Container


class DeleteContainer(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ContainerSerializer
    queryset = Container
