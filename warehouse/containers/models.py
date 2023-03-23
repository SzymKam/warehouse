from django.db import models
from .constants import (
    VENTILATION_MASK_SIZE,
    O2_MASK_SIZE,
    O2_MASK_TYPE,
    BLADE_SIZE,
    ET_TUBE_SIZE,
    OPA_TUBE_SIZE,
    NPA_TUBE_SIZE,
    GAUZE_SIZE,
    STERILE_GLOVES_SIZE,
    GLOVES_SIZE,
    LT_TUBE_SIZE,
    BIG_SIZE,
    SYRINGE_VOLUME,
    NEEDLE_SIZE,
    CANNULA_SIZE,
    FLUID_VOLUME,
    DRUG_DOSAGE_FORM,
    DRUG_ACTIVE_SUBSTANCES,
    CONTAINER_NAME_CHOICES,
    MEDICAL_EQUIPMENT_EQUIPMENT_TYPE_CHOICES,
    MEDICAL_EQUIPMENT_NAME_CHOICES,
)


class Container(models.Model):
    name = models.CharField(max_length=50, choices=CONTAINER_NAME_CHOICES)
    description = models.TextField(blank=True, null=True)
    # have_container = models.ForeignKey(Container, blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.description}"


class MedicalEquipment(models.Model):
    """class for basic and basic with expiration date medical equipment"""

    name = models.CharField(max_length=50, choices=MEDICAL_EQUIPMENT_NAME_CHOICES)
    container = models.ForeignKey(
        Container,
        blank=True,
        null=True,
        on_delete=models.DO_NOTHING,
        related_name="equipment",
    )
    amount = models.IntegerField(null=True, blank=True)
    expiration_date = models.DateField(null=True, blank=True)
    equipment_type = models.CharField(
        null=True,
        blank=True,
        max_length=50,
        choices=MEDICAL_EQUIPMENT_EQUIPMENT_TYPE_CHOICES,
    )
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.description}"


"""classes below, are classes for special medical equipment, requires special field/s"""


class Drug(MedicalEquipment):
    active_substance = models.CharField(choices=DRUG_ACTIVE_SUBSTANCES, max_length=30)
    psychotropic_or_narcotic = models.BooleanField(default=False)
    dosage_form = models.CharField(
        choices=DRUG_DOSAGE_FORM, blank=True, null=True, max_length=20
    )


class Fluid(MedicalEquipment):
    volume = models.CharField(choices=FLUID_VOLUME, max_length=20)


class Cannula(MedicalEquipment):
    size = models.CharField(choices=CANNULA_SIZE, max_length=20)


class Needle(MedicalEquipment):
    size = models.CharField(choices=NEEDLE_SIZE, max_length=20)


class Syringe(MedicalEquipment):
    volume = models.CharField(choices=SYRINGE_VOLUME, max_length=20)


class BIG(MedicalEquipment):
    size = models.CharField(choices=BIG_SIZE, max_length=20)


class LTTube(MedicalEquipment):
    size = models.CharField(choices=LT_TUBE_SIZE, max_length=20)


class Gloves(MedicalEquipment):
    size = models.CharField(choices=GLOVES_SIZE, max_length=20)


class SterileGloves(MedicalEquipment):
    size = models.CharField(choices=STERILE_GLOVES_SIZE, max_length=20)


class Gauze(MedicalEquipment):
    size = models.CharField(choices=GAUZE_SIZE, max_length=20)


class NasopharyngealTube(MedicalEquipment):
    size = models.CharField(choices=NPA_TUBE_SIZE, max_length=20)


class OropharyngealTube(MedicalEquipment):
    size = models.CharField(choices=OPA_TUBE_SIZE, max_length=20)


class EndotrachealTube(MedicalEquipment):
    size = models.CharField(choices=ET_TUBE_SIZE, max_length=20)


class LaryngoscopeBlade(MedicalEquipment):
    size = models.CharField(choices=BLADE_SIZE, max_length=20)


class OxygenMask(MedicalEquipment):
    type = models.CharField(choices=O2_MASK_TYPE, max_length=20)
    size = models.CharField(choices=O2_MASK_SIZE, max_length=20)


class VentilationMask(MedicalEquipment):
    size = models.CharField(choices=VENTILATION_MASK_SIZE, max_length=20)
