from django.forms import ModelForm
from .models import StaffModel
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import DateInput


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
            "groups",
            "image",
        )
        widgets = {"qualifications_expiration_date": DateInput(attrs={"type": "date"})}


class StaffFormUpdate(ModelForm):
    class Meta:
        model = StaffModel
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "medical_qualifications",
            "position",
            "qualifications_expiration_date",
            "groups",
            "image",
        )
        widgets = {"qualifications_expiration_date": DateInput(attrs={"type": "date"})}


class StaffFormUser(ModelForm):
    class Meta:
        model = StaffModel
        fields = ("username", "email", "image")
