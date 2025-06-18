from django.db import models
from django.utils import timezone

class Role(models.Model):
    RoleId = models.AutoField(primary_key=True)
    RoleName = models.CharField(max_length=100)
    IsActive = models.BooleanField(default=True)

    def __str__(self):
        return self.RoleName

class Staff(models.Model):
    StaffId = models.AutoField(primary_key=True)
    FullName = models.CharField(max_length=100)
    Gender = models.CharField(max_length=10, default='Not Specified')
    JoiningDate = models.DateField(default=timezone.now)
    MobileNumber = models.CharField(max_length=15, default='0000000000')
    UserName = models.CharField(max_length=50, unique=True)
    Password = models.CharField(max_length=128)
    IsActive = models.BooleanField(default=True)

    def __str__(self):
        return self.FullName

class Specialization(models.Model):
    SpecializationId = models.AutoField(primary_key=True)
    SpecializationName = models.CharField(max_length=100)

    def __str__(self):
        return self.SpecializationName

class Doctor(models.Model):
    DoctorId = models.AutoField(primary_key=True)
    ConsultationFee = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    SpecializationId = models.ForeignKey(Specialization, on_delete=models.CASCADE)
    StaffId = models.OneToOneField(Staff, on_delete=models.CASCADE)
    IsActive = models.BooleanField(default=True)

    def __str__(self):
        return f"Dr. {self.StaffId.FullName}"

class Membership(models.Model):
    MembershipId = models.AutoField(primary_key=True)
    MembershipType = models.CharField(max_length=100)
    IsActive = models.BooleanField(default=True)

    def __str__(self):
        return self.MembershipType

class Patient(models.Model):
    PatientId = models.AutoField(primary_key=True)
    PatientName = models.CharField(max_length=100)
    DateOfBirth = models.DateField()
    Gender = models.CharField(max_length=10, default='Not Specified')
    MobileNumber = models.CharField(max_length=15, default='0000000000')
    Address = models.TextField(default='Not Provided')
    MembershipId = models.ForeignKey(Membership, on_delete=models.CASCADE)
    IsActive = models.BooleanField(default=True)

    def __str__(self):
        return self.PatientName

class Appointment(models.Model):
    AppointmentId = models.AutoField(primary_key=True)
    AppointmentDate = models.DateTimeField(default=timezone.now)
    TokenNumber = models.IntegerField(default=0)
    ConsultationStatus = models.CharField(max_length=50, default='Pending')
    PatientId = models.ForeignKey(Patient, on_delete=models.CASCADE)
    DoctorId = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    IsActive = models.BooleanField(default=True)

    def __str__(self):
        return f"Appointment {self.AppointmentId} - {self.AppointmentDate}"

class MedicineCategory(models.Model):
    MedicineCategoryId = models.AutoField(primary_key=True)
    MedicineCategoryName = models.CharField(max_length=100)

    def __str__(self):
        return self.MedicineCategoryName

class Medicine(models.Model):
    MedicineId = models.AutoField(primary_key=True)
    MedicineName = models.CharField(max_length=100)
    ManufacturingDate = models.DateField(default=timezone.now)
    ExpiryDate = models.DateField()
    Unit = models.CharField(max_length=50, default='Box')
    MedicineCategoryId = models.ForeignKey(MedicineCategory, on_delete=models.CASCADE)
    IsActive = models.BooleanField(default=True)

    def __str__(self):
        return self.MedicineName

class MedicinePrescription(models.Model):
    MedicinePrescriptionId = models.AutoField(primary_key=True)
    MedicineId = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    Dosage = models.CharField(max_length=50, default='1 tablet')
    Frequency = models.CharField(max_length=50, default='Once a day')
    Duration = models.CharField(max_length=50, default='5 days')
    AppointmentId = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    IsActive = models.BooleanField(default=True)

class Consultation(models.Model):
    ConsultationId = models.AutoField(primary_key=True)
    Symptoms = models.TextField(default='N/A')
    Diagnosis = models.TextField(default='N/A')
    Notes = models.TextField(default='N/A')
    CreatedDate = models.DateTimeField(auto_now_add=True)
    AppointmentId = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    IsActive = models.BooleanField(default=True)

class MedicineStock(models.Model):
    MedicineStockId = models.AutoField(primary_key=True)
    StockInHand = models.IntegerField(default=0)
    ReOrderLevel = models.IntegerField(default=10)
    Purchase = models.IntegerField(default=0)
    Issuance = models.IntegerField(default=0)
    MedicineId = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    CreatedDate = models.DateField(default=timezone.now)
    IsActive = models.BooleanField(default=True)

class LabTestCategory(models.Model):
    LabTestCategoryId = models.AutoField(primary_key=True)
    LabTestCategoryName = models.CharField(max_length=100)

    def __str__(self):
        return self.LabTestCategoryName

class LabTest(models.Model):
    LabTestId = models.AutoField(primary_key=True)
    TestName = models.CharField(max_length=100)
    Amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    ReferenceMinRange = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    ReferenceMaxRange = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    SampleRequired = models.CharField(max_length=100, default='Blood')
    LabTestCategoryId = models.ForeignKey(LabTestCategory, on_delete=models.CASCADE)
    IsActive = models.BooleanField(default=True)

    def __str__(self):
        return self.TestName

class LabTestPrescription(models.Model):
    LabTestPrescriptionId = models.AutoField(primary_key=True)
    LabTestId = models.ForeignKey(LabTest, on_delete=models.CASCADE)
    LabTestValue = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    Remarks = models.TextField(default='Pending review')
    AppointmentId = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    IsActive = models.BooleanField(default=True)
