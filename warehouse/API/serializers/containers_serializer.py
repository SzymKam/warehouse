from rest_framework import serializers
from containers.models import Container
from .equipment_serializer import AllEquipmentSerializer
from API.constants import API_NAME_CHOICES


class ContainerSerializer(serializers.ModelSerializer):
    # def create(self, validated_data):
    #     name = validated_data.get('name')
    #     allowed_name = API_NAME_CHOICES
    #     if name in allowed_name:
    #         return super().create(validated_data)
    #     else:
    #         return serializers.ValidationError

    class Meta:
        model = Container
        fields = "__all__"


class DetailContainerSerializer(serializers.ModelSerializer, AllEquipmentSerializer):
    class Meta:
        model = Container
        fields = "__all__"
