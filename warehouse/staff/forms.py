from django.forms import ModelForm
from .models import StaffModel
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class StaffFormAdmin(UserCreationForm):
    class Meta:
        model = StaffModel
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
            "medical_qualifications",
            "position",
            "qualifications_expiration_date",
            "can_edit",
            "image",
        )


class StaffFormUser(ModelForm):
    class Meta:
        model = StaffModel
        fields = ("username", "email", "image")
