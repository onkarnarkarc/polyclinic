from django.contrib import admin
from .models import Doctor, Appointment, DoctorAvailability, DoctorUnavailability
# Register your models here.


admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(DoctorAvailability)
admin.site.register(DoctorUnavailability)
