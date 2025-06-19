from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from CMSapp.models import Consultation, MedicinePrescription, Appointment
from .serializers import ConsultationSerializer, MedicinePrescriptionSerializer

@api_view(['GET'])
def consultation_history_by_patient(request, patient_id):
    appointments = Appointment.objects.filter(PatientId=patient_id, IsActive=True)
    consultations = Consultation.objects.filter(AppointmentId__in=appointments, IsActive=True)
    serializer = ConsultationSerializer(consultations, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def consultation_history_by_doctor(request, doctor_id):
    appointments = Appointment.objects.filter(DoctorId=doctor_id, IsActive=True)
    consultations = Consultation.objects.filter(AppointmentId__in=appointments, IsActive=True)
    serializer = ConsultationSerializer(consultations, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def prescription_history_by_patient(request, patient_id):
    appointments = Appointment.objects.filter(PatientId=patient_id, IsActive=True)
    prescriptions = MedicinePrescription.objects.filter(AppointmentId__in=appointments, IsActive=True)
    serializer = MedicinePrescriptionSerializer(prescriptions, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def prescription_history_by_doctor(request, doctor_id):
    appointments = Appointment.objects.filter(DoctorId=doctor_id, IsActive=True)
    prescriptions = MedicinePrescription.objects.filter(AppointmentId__in=appointments, IsActive=True)
    serializer = MedicinePrescriptionSerializer(prescriptions, many=True)
    return Response(serializer.data)
