from rest_framework import serializers
from containers.models import Container
from .equipment_serializer import AllEquipmentSerializer


class AllContainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Container
        fields = "__all__"


class SingleContainerSerializer(serializers.ModelSerializer, AllEquipmentSerializer):
    class Meta:
        model = Container
        fields = "__all__"
