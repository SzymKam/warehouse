from rest_framework import serializers
from staff.models import StaffModel


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffModel
        # fields = ("username",
        #     "first_name",
        #     "last_name",
        #     "email",
        #     "password1",
        #     "password2",
        #     "medical_qualifications",
        #     "position",
        #     "qualifications_expiration_date",
        #     "groups",
        #     "image")
        fields = "__all__"
