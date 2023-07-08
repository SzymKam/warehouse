import datetime
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
)


class Container(models.Model):
    name = models.CharField(max_length=50, choices=CONTAINER_NAME_CHOICES)
    description = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"


def get_main_container():
    return Container.objects.get(name="Main core")


class BaseMedicalEquipment(models.Model):
    """abstract class working as a base for other models"""

    name = models.CharField(max_length=50)
    container = models.ForeignKey(
        Container,
        blank=True,
        null=True,
        on_delete=models.SET(get_main_container),
        related_name="base_medical_equipment",
        default=get_main_container,
    )
    amount = models.IntegerField(null=True, blank=True)
    expiration_date = models.DateField(null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    model_name = __name__

    @property
    def expiration_days(self):
        if self.expiration_date:
            delta_time = self.expiration_date - datetime.date.today()
            return delta_time.days
        return " "

    def __str__(self):
        return f"{self.name}"

    class Meta:
        abstract = True


class MedicalEquipment(BaseMedicalEquipment):
    """class for base / common temporary with no special fields"""

    container = models.ForeignKey(
        Container,
        blank=True,
        null=True,
        on_delete=models.SET(get_main_container),
        related_name="medical_equipment",
        default=get_main_container,
    )


"""classes below, are classes for special medical temporary, requires special field/s"""


class Drug(BaseMedicalEquipment):
    active_substance = models.CharField(choices=DRUG_ACTIVE_SUBSTANCES, max_length=30)
    psychotropic_or_narcotic = models.BooleanField(default=False)
    dosage_form = models.CharField(
        choices=DRUG_DOSAGE_FORM, blank=True, null=True, max_length=20
    )
    container = models.ForeignKey(
        Container,
        blank=True,
        null=True,
        on_delete=models.SET(get_main_container),
        related_name="drug",
        default=get_main_container,
    )


class Fluid(BaseMedicalEquipment):
    volume = models.CharField(choices=FLUID_VOLUME, max_length=20)
    container = models.ForeignKey(
        Container,
        blank=True,
        null=True,
        on_delete=models.SET(get_main_container),
        related_name="fluid",
        default=get_main_container,
    )


class Cannula(BaseMedicalEquipment):
    size = models.CharField(choices=CANNULA_SIZE, max_length=20)
    container = models.ForeignKey(
        Container,
        blank=True,
        null=True,
        on_delete=models.SET(get_main_container),
        related_name="cannula",
        default=get_main_container,
    )


class Needle(BaseMedicalEquipment):
    size = models.CharField(choices=NEEDLE_SIZE, max_length=20)
    container = models.ForeignKey(
        Container,
        blank=True,
        null=True,
        on_delete=models.SET(get_main_container),
        related_name="needle",
        default=get_main_container,
    )


class Syringe(BaseMedicalEquipment):
    volume = models.CharField(choices=SYRINGE_VOLUME, max_length=20)
    container = models.ForeignKey(
        Container,
        blank=True,
        null=True,
        on_delete=models.SET(get_main_container),
        related_name="syringe",
        default=get_main_container,
    )


class BIG(BaseMedicalEquipment):
    size = models.CharField(choices=BIG_SIZE, max_length=20)
    container = models.ForeignKey(
        Container,
        blank=True,
        null=True,
        on_delete=models.SET(get_main_container),
        related_name="big",
        default=get_main_container,
    )


class LtTube(BaseMedicalEquipment):
    size = models.CharField(choices=LT_TUBE_SIZE, max_length=20)
    container = models.ForeignKey(
        Container,
        blank=True,
        null=True,
        on_delete=models.SET(get_main_container),
        related_name="lt_tube",
        default=get_main_container,
    )


class Gloves(BaseMedicalEquipment):
    size = models.CharField(choices=GLOVES_SIZE, max_length=20)
    container = models.ForeignKey(
        Container,
        blank=True,
        null=True,
        on_delete=models.SET(get_main_container),
        related_name="gloves",
        default=get_main_container,
    )


class SterileGloves(BaseMedicalEquipment):
    size = models.CharField(choices=STERILE_GLOVES_SIZE, max_length=20)
    container = models.ForeignKey(
        Container,
        blank=True,
        null=True,
        on_delete=models.SET(get_main_container),
        related_name="sterile_gloves",
        default=get_main_container,
    )


class Gauze(BaseMedicalEquipment):
    size = models.CharField(choices=GAUZE_SIZE, max_length=20)
    container = models.ForeignKey(
        Container,
        blank=True,
        null=True,
        on_delete=models.SET(get_main_container),
        related_name="gauze",
        default=get_main_container,
    )


class NasopharyngealTube(BaseMedicalEquipment):
    size = models.CharField(choices=NPA_TUBE_SIZE, max_length=20)
    container = models.ForeignKey(
        Container,
        blank=True,
        null=True,
        on_delete=models.SET(get_main_container),
        related_name="nasopharyngeal_tube",
        default=get_main_container,
    )


class OropharyngealTube(BaseMedicalEquipment):
    size = models.CharField(choices=OPA_TUBE_SIZE, max_length=20)
    container = models.ForeignKey(
        Container,
        blank=True,
        null=True,
        on_delete=models.SET(get_main_container),
        related_name="oropharyngeal_tube",
        default=get_main_container,
    )


class EndotrachealTube(BaseMedicalEquipment):
    size = models.CharField(choices=ET_TUBE_SIZE, max_length=20)
    container = models.ForeignKey(
        Container,
        blank=True,
        null=True,
        on_delete=models.SET(get_main_container),
        related_name="endotracheal_tube",
        default=get_main_container,
    )


class LaryngoscopeBlade(BaseMedicalEquipment):
    size = models.CharField(choices=BLADE_SIZE, max_length=20)
    container = models.ForeignKey(
        Container,
        blank=True,
        null=True,
        on_delete=models.SET(get_main_container),
        related_name="laryngoscope_blade",
        default=get_main_container,
    )


class OxygenMask(BaseMedicalEquipment):
    type = models.CharField(choices=O2_MASK_TYPE, max_length=20)
    size = models.CharField(choices=O2_MASK_SIZE, max_length=20)
    container = models.ForeignKey(
        Container,
        blank=True,
        null=True,
        on_delete=models.SET(get_main_container),
        related_name="oxygen_mask",
        default=get_main_container,
    )


class VentilationMask(BaseMedicalEquipment):
    size = models.CharField(choices=VENTILATION_MASK_SIZE, max_length=20)
    container = models.ForeignKey(
        Container,
        blank=True,
        null=True,
        on_delete=models.SET(get_main_container),
        related_name="ventilation_mask",
        default=get_main_container,
    )
