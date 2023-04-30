from django.db import models
from django.contrib.auth.models import AbstractUser
from .constants import QUALIFICATIONS


class StaffModel(AbstractUser):
    position = models.CharField(
        max_length=50, blank=True, null=True, help_text="role in GRM"
    )
    medical_qualifications = models.CharField(
        max_length=50,
        choices=QUALIFICATIONS,
        default="First aid",
        help_text="Qualifications",
    )
    qualifications_expiration_date = models.DateField(blank=True, null=True)
    image = models.ImageField(default="grm_logo.jpg", upload_to="profile_pictures")

    def __str__(self):
        return f"{self.username} - {self.medical_qualifications}, {self.position}"
