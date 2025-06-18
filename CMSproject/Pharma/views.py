from rest_framework import viewsets
from .models import *
from .Serializers import *
from rest_framework.response import Response
from rest_framework.decorators import action


class MedicineCategoryViewSet(viewsets.ModelViewSet):
    queryset = MedicineCategory.objects.all()
    serializer_class = MedicineCategorySerializer

class MedicineViewSet(viewsets.ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer

class MedicineStockViewSet(viewsets.ModelViewSet):
    queryset = MedicineStock.objects.all()
    serializer_class = MedicineStockSerializer
    @action(detail=False, methods=['get'])
    def low_stock(self, request):
        low_stocks = self.queryset.filter(stock_in_hand__lte=models.F('reorder_level'))
        serializer = self.get_serializer(low_stocks, many=True)
        return Response(serializer.data)

class MedicinePrescriptionViewSet(viewsets.ModelViewSet):
    queryset = MedicinePrescription.objects.all()
    serializer_class = MedicinePrescriptionSerializer