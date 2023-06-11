from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView,
)
from API.serializers.containers_serializer import (
    AllContainerSerializer,
    SingleContainerSerializer,
)
from containers.models import Container
from rest_framework.permissions import IsAuthenticated


class GetAllContainers(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AllContainerSerializer
    queryset = Container.objects.all()


class GetContainer(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SingleContainerSerializer
    queryset = Container


class CreateContainer(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SingleContainerSerializer
    # todo add name verification to create container -> error when name is not on list


class UpdateContainer(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SingleContainerSerializer
    queryset = Container
    # todo add name verification to update container -> error when name is not on list


class DeleteContainer(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SingleContainerSerializer
    queryset = Container
