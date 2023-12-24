# Create your models here.

from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='doctor_images/', null=True, blank=True)

    mobile_number = models.CharField(max_length=15,null = True,blank = True)
    age = models.IntegerField(null = True,blank = True)
    day_of_appointment = models.CharField(max_length = 100,null = True,blank = True)
    time_of_appointment = models.TimeField(null = True,blank = True)
    not_available = models.BooleanField(default = False) 
class VisitType(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default = True)

    def __str__(self):
        return self.name



class Appointment(models.Model):
    patient_name = models.CharField(max_length=100)
    age = models.IntegerField(null = True)
    mobile_number = models.CharField(max_length=15,null = True,blank = True)
    date_of_appointment = models.DateField(null = True,blank = True)
    time_of_appointment = models.TimeField(null = True,blank = True)
    # type_of_visit = models.CharField(max_length=100)
    type_of_visit = models.ForeignKey(VisitType, on_delete=models.DO_NOTHING,blank = True, null = True)
    doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING)

