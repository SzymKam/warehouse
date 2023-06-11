from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView,
)
from API.serializers.staff_serialzer import StaffSerializer
from staff.models import StaffModel
from rest_framework.permissions import IsAuthenticated


class GetAllStaff(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StaffSerializer
    queryset = StaffModel.objects.all()


class GetStaff(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StaffSerializer
    queryset = StaffModel


class CreateStaff(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StaffSerializer


class UpdateStaff(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StaffSerializer
    queryset = StaffModel


class DeleteStaff(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StaffSerializer
    queryset = StaffModel
