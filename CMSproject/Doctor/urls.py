from django.urls import path
from . import views

urlpatterns = [
    path('consultations/patient/<int:patient_id>/', views.consultation_history_by_patient),
    path('consultations/doctor/<int:doctor_id>/', views.consultation_history_by_doctor),
    path('prescriptions/patient/<int:patient_id>/', views.prescription_history_by_patient),
    path('prescriptions/doctor/<int:doctor_id>/', views.prescription_history_by_doctor),
]
