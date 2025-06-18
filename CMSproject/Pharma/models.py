from django.db import models
from CMSapp.models import Appointment


class Medicine(models.Model):
    MedicineId = models.AutoField(primary_key=True)
    MedicineName = models.CharField(max_length=100)
    ManufacturingDate = models.DateField()
    ExpiryDate = models.DateField()
    Unit = models.CharField(max_length=50)
    IsActive = models.BooleanField(default=True)

    def __str__(self):
        return self.MedicineName

class MedicineStock(models.Model):
    MedicineStockId = models.AutoField(primary_key=True)
    StockInHand = models.IntegerField()
    ReOrderLevel = models.IntegerField()
    Purchase = models.IntegerField()
    Issuance = models.IntegerField()
    MedicineId = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    CreatedDate = models.DateField(auto_now_add=True)
    IsActive = models.BooleanField(default=True)

class MedicineCategory(models.Model):
    MedicineCategoryId = models.AutoField(primary_key=True)
    MedicineCategoryName = models.CharField(max_length=100)

    def __str__(self):
        return self.MedicineCategoryName
    

class MedicinePrescription(models.Model):
    MedicinePrescriptionId = models.AutoField(primary_key=True)
    MedicineId = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    Dosage = models.CharField(max_length=50)
    Frequency = models.CharField(max_length=50)
    Duration = models.CharField(max_length=50)
    AppointmentId = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='pharma_prescriptions')

 # Change this if you use Appointment model
    IsActive = models.BooleanField(default=True)

    def __str__(self):
        return f"Prescription {self.MedicinePrescriptionId} for {self.MedicineId.MedicineName}"