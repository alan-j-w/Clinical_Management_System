from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'categories', MedicineCategoryViewSet)
router.register(r'medicines', MedicineViewSet)
router.register(r'stocks', MedicineStockViewSet)
router.register(r'prescriptions', MedicinePrescriptionViewSet)

urlpatterns = router.urls