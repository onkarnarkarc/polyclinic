from django.contrib import admin
from .models import Doctor, Appointment, DoctorAvailability, DoctorUnavailability
# Register your models here.
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class DoctorResource(resources.ModelResource):
	class Meta:
		model = Doctor
		fields = ('name','specialization','mobile_number','day_of_appointment')
class DoctorAdmin(ImportExportModelAdmin):
	list_display = ('name','specialization','mobile_number','day_of_appointment')
	list_display_links = ('name',)
	resource_class = DoctorResource
	search_fields = ('name', 'specialization','mobile_number','day_of_appointment')
	list_per_page = 50
admin.site.register(Doctor,DoctorAdmin)

class AppointmentResource(resources.ModelResource):
	class Meta:
		model = Appointment
		fields = ('id','patient_name','age','mobile_number','date_of_appointment','selected_time_slot','doctor')

class AppointmentAdmin(ImportExportModelAdmin):
	list_display = ('id','patient_name','age','mobile_number','date_of_appointment','selected_time_slot','doctor')
	list_display_links = ('id',)
	resource_class = AppointmentResource
	search_fields = ('patient_name', 'age','mobile_number','doctor__name')
	list_per_page = 50


admin.site.register(Appointment,AppointmentAdmin)

class DoctorAvailabilityResource(resources.ModelResource):
	class Meta:
		model = DoctorAvailability
		fields = ('id','doctor','day_of_week','start_time_of_availability','end_time_of_availability')

class DoctorAvailabilityAdmin(ImportExportModelAdmin):
	list_display = ('id','doctor','day_of_week','start_time_of_availability','end_time_of_availability')
	list_display_links = ('id',)
	resource_class = DoctorAvailabilityResource
	search_fields = ('doctor__name', 'day_of_week')
	list_per_page = 50


admin.site.register(DoctorAvailability,DoctorAvailabilityAdmin)

class DoctorUnavailabilityResource(resources.ModelResource):
	class Meta:
		model = DoctorUnavailability
		fields = ('id','unavailable_slot','date')

class DoctorAvailabilityAdmin(ImportExportModelAdmin):
	list_display = ('id','unavailable_slot','date')
	list_display_links = ('id',)
	resource_class = DoctorUnavailabilityResource
	search_fields = ('date',)
	list_per_page = 50
admin.site.register(DoctorUnavailability,DoctorAvailabilityAdmin)
