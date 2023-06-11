from rest_framework import serializers
from containers.models import Container
from staff.models import StaffModel


class ContainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Container
        fields = "__all__"


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
