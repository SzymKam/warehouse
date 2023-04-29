from django.db import models
from django.contrib.auth.models import User
from .constants import QUALIFICATIONS


class Staff(User):
    position = models.CharField(
        max_length=50, blank=True, null=True, help_text="role in GRM"
    )
    image = models.ImageField(default="grm_logo.jpg")
    medical_qualifications = models.CharField(
        max_length=50,
        choices=QUALIFICATIONS,
        default="First aid",
        help_text="Qualifications",
    )
    qualifications_expiration_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.username} - {self.medical_qualifications}"
