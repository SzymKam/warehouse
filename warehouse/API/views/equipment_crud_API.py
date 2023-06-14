from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView,
)
from API.serializers.equipment_serializer import (
    AllEquipmentSerializer,
    MedicalEquipmentSerializer,
)
from rest_framework.permissions import IsAuthenticated
from containers.models import MedicalEquipment, Drug
from API.constants import SERIALIZER_DICT, serializer_drugs_and_fluids


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
    serializer_class = MedicalEquipmentSerializer

    @staticmethod
    def get_class_serializer(name_value):
        print("name value", name_value)
        serializer_dict = serializer_drugs_and_fluids()
        try:
            serializer = serializer_dict[name_value]
            print("after dict", serializer)
        except KeyError:
            serializer = MedicalEquipmentSerializer
        print("end", serializer)
        return serializer

    def get_serializer(self, *args, **kwargs):
        name_value = self.request.data["name"]
        # serializer_class = self.get_serializer_class()
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
