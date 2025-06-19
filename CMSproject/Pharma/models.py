from django.db import models
from django.utils import timezone

class MedicineCategory(models.Model):
    name = models.CharField(max_length=100)

    def _str_(self):
        return self.name

class Medicine(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('expired', 'Expired'),
        ('inactive', 'Inactive'),
    ]
    name = models.CharField(max_length=100)
    category = models.ForeignKey(MedicineCategory, on_delete=models.CASCADE)
    manufacturing_date = models.DateField()
    expiry_date = models.DateField()
    unit = models.CharField(max_length=20)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    is_active = models.BooleanField(default=True)

    def update_status(self):
        if self.expiry_date < timezone.now().date():
            self.status = 'expired'
            self.save()

    def _str_(self):
        return f"{self.name} - {self.status}"

class MedicineStock(models.Model):
    medicine = models.OneToOneField(Medicine, on_delete=models.CASCADE)
    stock_in_hand = models.IntegerField()
    reorder_level = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)

    def is_low_stock(self):
        return self.stock_in_hand <= self.reorder_level

class MedicinePrescription(models.Model):
    appointment_id = models.IntegerField()  # ForeignKey if appointments are implemented
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    dosage = models.CharField(max_length=100)
    frequency = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)