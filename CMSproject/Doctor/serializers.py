from rest_framework import serializers
from CMSapp.models import Consultation, MedicinePrescription

class ConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation
        fields = '__all__'

class MedicinePrescriptionSerializer(serializers.ModelSerializer):
    medicine_name = serializers.CharField(source='MedicineId.MedicineName', read_only=True)

    class Meta:
        model = MedicinePrescription
        fields = ['MedicinePrescriptionId', 'medicine_name', 'Dosage', 'Frequency', 'Duration', 'AppointmentId']
