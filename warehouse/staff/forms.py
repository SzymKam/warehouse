from django.forms import ModelForm
from .models import Staff
from django.contrib.auth.forms import UserCreationForm


class StaffForm(ModelForm):
    class Meta:
        model = Staff
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "medical_qualifications",
            "qualifications_expiration_date",
            "position",
            "is_staff",
            "is_active",
            "image",
        ]


#

#
# class StaffForm(UserCreationForm):
#     class Meta:
#         model = Staff
#         fields = "__all__"
