from rest_framework.viewsets import ModelViewSet
from API.serializers.staff_serialzer import StaffSerializer
from staff.models import StaffModel
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions


class StaffViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    serializer_class = StaffSerializer
    queryset = StaffModel.objects.all()
