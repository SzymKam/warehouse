from rest_framework import serializers
from rest_framework.serializers import Serializer

from containers.models import (
    MedicalEquipment,
    Drug,
    Fluid,
    Cannula,
    Needle,
    Syringe,
    BIG,
    LtTube,
    Gloves,
    SterileGloves,
    Gauze,
    NasopharyngealTube,
    OropharyngealTube,
    EndotrachealTube,
    LaryngoscopeBlade,
    OxygenMask,
    VentilationMask,
)


class MedicalEquipmentSerializer(serializers.ModelSerializer):
    expiration_days = serializers.CharField(read_only=True)

    class Meta:
        model = MedicalEquipment
        fields = "__all__"


class DrugSerializer(serializers.ModelSerializer):
    expiration_days = serializers.CharField(read_only=True)

    class Meta:
        model = Drug
        fields = "__all__"


class FluidSerializer(serializers.ModelSerializer):
    expiration_days = serializers.CharField(read_only=True)

    class Meta:
        model = Fluid
        fields = "__all__"


class CannulaSerializer(serializers.ModelSerializer):
    expiration_days = serializers.CharField(read_only=True)

    class Meta:
        model = Cannula
        fields = "__all__"


class NeedleSerializer(serializers.ModelSerializer):
    expiration_days = serializers.CharField(read_only=True)

    class Meta:
        model = Needle
        fields = "__all__"


class SyringeSerializer(serializers.ModelSerializer):
    expiration_days = serializers.CharField(read_only=True)

    class Meta:
        model = Syringe
        fields = "__all__"


class BIGSerializer(serializers.ModelSerializer):
    expiration_days = serializers.CharField(read_only=True)

    class Meta:
        model = BIG
        fields = "__all__"


class LtTubeSerializer(serializers.ModelSerializer):
    expiration_days = serializers.CharField(read_only=True)

    class Meta:
        model = LtTube
        fields = "__all__"


class GlovesSerializer(serializers.ModelSerializer):
    expiration_days = serializers.CharField(read_only=True)

    class Meta:
        model = Gloves
        fields = "__all__"


class SterileGlovesSerializer(serializers.ModelSerializer):
    expiration_days = serializers.CharField(read_only=True)

    class Meta:
        model = SterileGloves
        fields = "__all__"


class GauzeSerializer(serializers.ModelSerializer):
    expiration_days = serializers.CharField(read_only=True)

    class Meta:
        model = Gauze
        fields = "__all__"


class NasopharyngealTubeSerializer(serializers.ModelSerializer):
    expiration_days = serializers.CharField(read_only=True)

    class Meta:
        model = NasopharyngealTube
        fields = "__all__"


class OropharyngealTubeSerializer(serializers.ModelSerializer):
    expiration_days = serializers.CharField(read_only=True)

    class Meta:
        model = OropharyngealTube
        fields = "__all__"


class EndotrachealTubeSerializer(serializers.ModelSerializer):
    expiration_days = serializers.CharField(read_only=True)

    class Meta:
        model = EndotrachealTube
        fields = "__all__"


class LaryngoscopeBladeSerializer(serializers.ModelSerializer):
    expiration_days = serializers.CharField(read_only=True)

    class Meta:
        model = LaryngoscopeBlade
        fields = "__all__"


class OxygenMaskSerializer(serializers.ModelSerializer):
    expiration_days = serializers.CharField(read_only=True)

    class Meta:
        model = OxygenMask
        fields = "__all__"


class VentilationMaskSerializer(serializers.ModelSerializer):
    expiration_days = serializers.CharField(read_only=True)

    class Meta:
        model = VentilationMask
        fields = "__all__"


class AllEquipmentSerializer(Serializer):
    """
    Serializer with all equipments items combined.

    """

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        serializers_dict = {
            "drug": DrugSerializer(Drug.objects.all(), many=True).data,
            "medical_equipment": MedicalEquipmentSerializer(
                MedicalEquipment.objects.all(), many=True
            ).data,
            "fluid": FluidSerializer(Fluid.objects.all(), many=True).data,
            "cannula": CannulaSerializer(Cannula.objects.all(), many=True).data,
            "needle": NeedleSerializer(Needle.objects.all(), many=True).data,
            "syringe": SyringeSerializer(Syringe.objects.all(), many=True).data,
            "big": BIGSerializer(BIG.objects.all(), many=True).data,
            "lt_tube": LtTubeSerializer(LtTube.objects.all(), many=True).data,
            "gloves": GlovesSerializer(Gloves.objects.all(), many=True).data,
            "sterile_gloves": SterileGlovesSerializer(
                SterileGloves.objects.all(), many=True
            ).data,
            "gauze": GauzeSerializer(Gauze.objects.all(), many=True).data,
            "npa_tube": NasopharyngealTubeSerializer(
                NasopharyngealTube.objects.all(), many=True
            ).data,
            "opa_tube": OropharyngealTubeSerializer(
                OropharyngealTube.objects.all(), many=True
            ).data,
            "et_tube": EndotrachealTubeSerializer(
                EndotrachealTube.objects.all(), many=True
            ).data,
            "laryngoscope_blade": LaryngoscopeBladeSerializer(
                LaryngoscopeBlade.objects.all(), many=True
            ).data,
            "oxygen_mask": OxygenMaskSerializer(
                OxygenMask.objects.all(), many=True
            ).data,
            "ventilation_mask": VentilationMaskSerializer(
                VentilationMask.objects.all(), many=True
            ).data,
        }
        representation.update(serializers_dict)
        return representation
