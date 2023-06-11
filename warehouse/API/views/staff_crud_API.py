from rest_framework.viewsets import ModelViewSet
from API.serializers.staff_serialzer import StaffSerializer
from staff.models import StaffModel
from rest_framework.permissions import IsAuthenticated


class StaffViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = StaffSerializer
    queryset = StaffModel.objects.all()
