from rest_framework import viewsets
from Administrator.models import Staff, Doctor
from .Serializers import StaffSerializer, DoctorSerializer

class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
