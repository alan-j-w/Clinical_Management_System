from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    MedicineViewSet,
    MedicineCategoryViewSet,
    MedicineStockViewSet,
    MedicinePrescriptionViewSet
)

router = DefaultRouter()
router.register(r'medicines', MedicineViewSet)
router.register(r'medicine-categories', MedicineCategoryViewSet)
router.register(r'medicine-stock', MedicineStockViewSet)
router.register(r'medicine-prescriptions', MedicinePrescriptionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
