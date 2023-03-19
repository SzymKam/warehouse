from django.db import models

MEDICAL_EQUIPMENT_CONTAINER_CHOICES = []
MEDICAL_EQUIPMENT_NAME_CHOICES = []
MEDICAL_EQUIPMENT_EQUIPMENT_TYPE_CHOICES = []

CONTAINER_NAME_CHOICES = []


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
        max_length=50, choices=MEDICAL_EQUIPMENT_EQUIPMENT_TYPE_CHOICES
    )
    description = models.TextField(null=True, blank=True)
