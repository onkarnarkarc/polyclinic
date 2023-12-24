# your_app/filters.py
import django_filters
from .models import Appointment

class AppointmentFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(field_name='date_of_appointment', lookup_expr='gte')
    end_date = django_filters.DateFilter(field_name='date_of_appointment', lookup_expr='lte')
    doctor_name = django_filters.CharFilter(field_name='doctor__name', lookup_expr='icontains')

    class Meta:
        model = Appointment
        fields = ['start_date', 'end_date', 'doctor_name']
