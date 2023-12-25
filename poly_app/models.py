# Create your models here.
import uuid

from django.db import models


class Doctor(models.Model):
    id = models.UUIDField(primary_key=True, db_index=True, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='doctor_images/', null=True, blank=True)
    mobile_number = models.CharField(max_length=15, null=True, blank=True)
    date_of_birth = models.IntegerField(null=True, blank=True)
    day_of_appointment = models.CharField(max_length=100, null=True, blank=True)
    time_of_appointment = models.TimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)


class DoctorAvailability(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    doctor = models.ForeignKey(Doctor, null=False)
    day_of_week = models.CharField(max_length=10)
    start_time_of_availability = models.TimeField(null=False)
    end_time_of_availability = models.TimeField(null=False)
    is_active = models.BooleanField(default=True)


class DoctorUnavailability(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    unavailable_slot = models.ForeignKey(DoctorAvailability, null=False, blank=False, on_delete=models.SET_NULL)
    date = models.DateField(null=False)
    is_active = models.BooleanField(default=True)


class VisitType(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, db_index=True)
    patient_name = models.CharField(max_length=100, db_index=True)
    age = models.IntegerField(null=False)
    mobile_number = models.PositiveIntegerField(max_length=10, null=False, blank=False)
    date_of_appointment = models.DateField(null=False)
    time_of_appointment = models.TimeField(null=False, blank=False)
    doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING)
    selected_time_slot = models.ForeignKey(DoctorAvailability, on_delete=models.PROTECT)
    type_of_visit = models.ForeignKey(VisitType, on_delete=models.PROTECT, null=False)
    is_active = models.BooleanField(default=True)
