from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView,
)
from API.serializers import StaffSerializer
from staff.models import StaffModel


class GetAllStaff(ListAPIView):
    serializer_class = StaffSerializer
    queryset = StaffModel.objects.all()


class GetStaff(RetrieveAPIView):
    serializer_class = StaffSerializer
    queryset = StaffModel


class CreateStaff(CreateAPIView):
    serializer_class = StaffSerializer


class UpdateStaff(UpdateAPIView):
    serializer_class = StaffSerializer
    queryset = StaffModel


class DeleteStaff(DestroyAPIView):
    serializer_class = StaffSerializer
    queryset = StaffModel
