from django.shortcuts import render
from . import models
from .models import *
# Create your views here.
from .forms import AppointmentEntryForm, DoctorEnrollmentForm




def homepage(request):
    # Retrieve doctor portfolio
    print("hello")
    doctors = Doctor.objects.all()
    # doctors = {}
    return render(request, 'poly_app/homepage.html', {'doctors': doctors})

def appointment_entry(request):
    if request.method == 'POST':
        form = AppointmentEntryForm(request.POST)
        if form.is_valid():
            form.save()
            # Add any additional logic, e.g., send confirmation email
    else:
        form = AppointmentEntryForm()
    return render(request, 'poly_app/appointment_entry.html', {'form': form})

def doctor_enrollment(request):
    if request.method == 'POST':
        form = DoctorEnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            # Add any additional logic, e.g., send welcome email
    else:
        form = DoctorEnrollmentForm()
    return render(request, 'poly_app/doctor_enrollment.html', {'form': form})


# def appointment_dashboard(request):
#     pass
from .filter import AppointmentFilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def appointment_dashboard(request):
    appointment_list = Appointment.objects.all()
    appointment_filter = AppointmentFilter(request.GET, queryset=appointment_list)
    print("appointment_filter====================", appointment_filter.qs)
    appointment_filter = appointment_list.order_by('date_of_appointment')
    paginator = Paginator(appointment_filter, 10)  # Show 10 appointments per page
    page = request.GET.get('page')

    try:
        appointments = paginator.page(page)
    except PageNotAnInteger:
        appointments = paginator.page(1)
    except EmptyPage:
        appointments = paginator.page(paginator.num_pages)
    doctors = Doctor.objects.all()
    return render(request, 'poly_app/appointment_dashboard.html', {'filter': appointment_filter,'appointments': appointments, 'doctors': doctors})
