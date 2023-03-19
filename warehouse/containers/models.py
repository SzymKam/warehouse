from django.db import models

MEDICAL_EQUIPMENT_CONTAINER_CHOICES = []
MEDICAL_EQUIPMENT_NAME_CHOICES = []
MEDICAL_EQUIPMENT_EQUIPMENT_TYPE_CHOICES = []

CONTAINER_NAME_CHOICES = []

DRUG_ACTIVE_SUBSTANCES = []
DRUG_DOSAGE_FORM = []

FLUID_VOLUME = []

CANNULA_SIZE = []

NEEDLE_VOLUME = []

SYRINGE_SIZE = []

BIG_SIZE = []


class Container(models.Model):
    name = models.CharField(max_length=50, choices=CONTAINER_NAME_CHOICES)
    description = models.TextField(blank=True, null=True)
    # have_container = models.ForeignKey(Container, blank=True, null=True)


class MedicalEquipment(models.Model):
    """class for basic and basic with expiration date medical equipment"""

    name = models.CharField(max_length=50, choices=MEDICAL_EQUIPMENT_NAME_CHOICES)
    container = models.ForeignKey(
        Container,
        blank=True,
        null=True,
        on_delete=models.DO_NOTHING,
        choices=MEDICAL_EQUIPMENT_CONTAINER_CHOICES,
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


class Drug(MedicalEquipment):
    active_substance = models.CharField(choices=DRUG_ACTIVE_SUBSTANCES)
    psychotropic_or_narcotic = models.BooleanField()
    dosage_form = models.CharField(choices=DRUG_DOSAGE_FORM, blank=True, null=True)


class Fluid(MedicalEquipment):
    volume = models.CharField(choices=FLUID_VOLUME)


class Cannula(MedicalEquipment):
    size = models.CharField(choices=CANNULA_SIZE)


class Needle(MedicalEquipment):
    volume = models.CharField(choices=NEEDLE_VOLUME)


class Syringe(MedicalEquipment):
    size = models.CharField(choices=SYRINGE_SIZE)


class BIG:
    size = models.CharField(choices=BIG_SIZE)
