from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Medicine, MedicineCategory, MedicineStock, MedicinePrescription
from .Serializers import (
    MedicineSerializer,
    MedicineCategorySerializer,
    MedicineStockSerializer,
    MedicinePrescriptionSerializer
)

# Existing views
class MedicineViewSet(viewsets.ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer

class MedicineCategoryViewSet(viewsets.ModelViewSet):
    queryset = MedicineCategory.objects.all()
    serializer_class = MedicineCategorySerializer

# Step 2: Inventory View
class MedicineStockViewSet(viewsets.ModelViewSet):
    queryset = MedicineStock.objects.all()
    serializer_class = MedicineStockSerializer

    @action(detail=True, methods=['patch'])
    def flag_low(self, request, pk=None):
        stock = self.get_object()
        if stock.StockInHand <= stock.ReOrderLevel:
            return Response({'message': 'Stock is low'})
        else:
            return Response({'message': 'Stock is sufficient'})

# Step 3: Prescription View
class MedicinePrescriptionViewSet(viewsets.ModelViewSet):
    queryset = MedicinePrescription.objects.all()
    serializer_class = MedicinePrescriptionSerializer

    @action(detail=False, methods=['get'])
    def by_appointment(self, request):
        appointment_id = request.query_params.get('appointment_id')
        prescriptions = self.queryset.filter(AppointmentId=appointment_id)
        serializer = self.get_serializer(prescriptions, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def by_patient(self, request):
        patient_id = request.query_params.get('patient_id')
        prescriptions = self.queryset.filter(AppointmentId__PatientId=patient_id)
        serializer = self.get_serializer(prescriptions, many=True)
        return Response(serializer.data)
