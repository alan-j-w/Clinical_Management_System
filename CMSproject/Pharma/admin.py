from django.contrib import admin
from .models import Medicine, MedicineCategory, MedicineStock, MedicinePrescription

admin.site.register(MedicineCategory)
admin.site.register(Medicine)
admin.site.register(MedicineStock)
admin.site.register(MedicinePrescription)