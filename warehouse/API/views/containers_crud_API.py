from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView,
)
from API.serializers import ContainerSerializer
from containers.models import Container


class GetAllContainers(ListAPIView):
    serializer_class = ContainerSerializer
    queryset = Container.objects.all()


class GetContainer(RetrieveAPIView):
    serializer_class = ContainerSerializer
    queryset = Container


class CreateContainer(CreateAPIView):
    serializer_class = ContainerSerializer


class UpdateContainer(UpdateAPIView):
    serializer_class = ContainerSerializer
    queryset = Container


class DeleteContainer(DestroyAPIView):
    serializer_class = ContainerSerializer
    queryset = Container
