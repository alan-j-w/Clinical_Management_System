from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Administrator.views import StaffViewSet, DoctorViewSet

router = DefaultRouter()
router.register(r'staff', StaffViewSet, basename='staff')
router.register(r'doctors', DoctorViewSet, basename='doctors')

urlpatterns = [
    path('', include(router.urls)),
]
