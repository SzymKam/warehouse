from rest_framework import serializers
from rest_framework.serializers import Serializer, ModelSerializer
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
    class Meta:
        model = MedicalEquipment
        fields = "__all__"


class DrugSerializer(serializers.ModelSerializer):
    expiration_days = serializers.CharField(read_only=True)

    class Meta:
        model = Drug
        fields = "__all__"


class FluidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fluid
        fields = "__all__"


class CannulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cannula
        fields = "__all__"


class NeedleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Needle
        fields = "__all__"


class SyringeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Syringe
        fields = "__all__"


class BIGSerializer(serializers.ModelSerializer):
    class Meta:
        model = BIG
        fields = "__all__"


class LtTubeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LtTube
        fields = "__all__"


class GlovesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gloves
        fields = "__all__"


class SterileGlovesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SterileGloves
        fields = "__all__"


class GauzeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gauze
        fields = "__all__"


class NasopharyngealTubeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NasopharyngealTube
        fields = "__all__"


class OropharyngealTubeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OropharyngealTube
        fields = "__all__"


class EndotrachealTubeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EndotrachealTube
        fields = "__all__"


class LaryngoscopeBladeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LaryngoscopeBlade
        fields = "__all__"


class OxygenMaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = OxygenMask
        fields = "__all__"


class VentilationMaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = VentilationMask
        fields = "__all__"


class AllEquipmentSerializer(Serializer):
    """
    Serializer with all equipments items combined.

    """

    # medical_equipment = MedicalEquipmentSerializer(many=True, read_only=True)
    # drug = DrugSerializer(many=True, read_only=True)
    # fluid = FluidSerializer(many=True, read_only=True)
    # cannula = CannulaSerializer(many=True, read_only=True)
    # needle = NeedleSerializer(many=True, read_only=True)
    # syringe = SyringeSerializer(many=True, read_only=True)
    # big = BIGSerializer(many=True, read_only=True)
    # lt_tube = LtTubeSerializer(many=True, read_only=True)
    # gloves = GlovesSerializer(many=True, read_only=True)
    # sterile_gloves = SterileGlovesSerializer(many=True, read_only=True)
    # gauze = GauzeSerializer(many=True, read_only=True)
    # npa_tube = NasopharyngealTubeSerializer(many=True, read_only=True)
    # opa_tube = OropharyngealTubeSerializer(many=True, read_only=True)
    # et_tube = EndotrachealTubeSerializer(many=True, read_only=True)
    # laryngoscope_blade = LaryngoscopeBladeSerializer(many=True, read_only=True)
    # oxygen_mask = OxygenMaskSerializer(many=True, read_only=True)
    # ventilation_mask = VentilationMaskSerializer(many=True, read_only=True)

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        drug = DrugSerializer(Drug.objects.all(), many=True).data
        medical_equipment = MedicalEquipmentSerializer(
            MedicalEquipment.objects.all(), many=True
        ).data

        representation["drug"] = drug
        representation["medical_equipment"] = medical_equipment

        return representation
