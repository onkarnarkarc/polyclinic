from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('appointment/', views.appointment_entry, name='appointment_entry'),
    path('enroll-doctor/', views.doctor_enrollment, name='doctor_enrollment'),
    path('appointment_dashboard/', views.appointment_dashboard, name='appointment_dashboard'),
    path('dr_appointment_time_slot/', views.DrAppointmentSlotViewset.as_view(), name='dr_appointment_time_slot')
]