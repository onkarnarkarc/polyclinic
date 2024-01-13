# clinic/forms.py
from django import forms
from .models import Appointment, Doctor, DoctorAvailability, VisitType
from datetime import timezone
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator

import re
# import phonenumbers


def validate_mobile_number(value):
    """
    Validate that the given value is a valid mobile number.
    """
    # Remove any non-digit characters from the mobile number
    cleaned_mobile_number = ''.join(c for c in value if c.isdigit())

    # Check if the cleaned mobile number has at least 10 digits
    if len(cleaned_mobile_number) < 10:
        raise ValidationError('Mobile number must have at least 10 digits.')
from datetime import datetime, time, timedelta

# views.py
from datetime import datetime
from .models import DoctorUnavailability

def is_doctor_available(doctor, appointment_date, appointment_time):

    # Check if the doctor is active
    if not doctor.is_active:
        return False

    # Find the day of the week for the appointment date
    appointment_day_of_week = appointment_date.strftime('%A').lower()

    # Check if the doctor has availability on the specified day of the week
    doctor_availability = doctor.doctoravailability_set.filter(
        day_of_week=appointment_day_of_week,
        is_active=True
    ).first()

    # Check if the doctor is explicitly marked as unavailable for the specified date
    doctor_unavailability = DoctorUnavailability.objects.filter(
        unavailable_slot__doctor=doctor,
        date=appointment_date,
        is_active=True
    ).exists()

    # if doctor_unavailability:
        

    if doctor_availability and not doctor_unavailability:
        # Check if the appointment time is within the doctor's available time range
        start_time = doctor_availability.start_time_of_availability
        end_time = doctor_availability.end_time_of_availability

        if start_time <= appointment_time <= end_time:
            # Check if there is already an appointment scheduled for the specified date and time
            conflicting_appointment = doctor.appointment_set.filter(
                date_of_appointment=appointment_date,
                time_of_appointment=appointment_time,
                is_active=True
            ).first()

            if not conflicting_appointment:
                # If all checks pass, the doctor is available
                return True

    # If any of the checks fail, the doctor is not available
    return False

class DateInput(forms.DateInput):
    input_type = 'date'

class VisitTypeForm(forms.ModelForm):
    class Meta:
        model = VisitType
        fields = ['name']


class AppointmentEntryForm(forms.ModelForm):
    time_of_appointment = forms.ModelChoiceField(
        queryset=DoctorAvailability.objects.filter(is_active=True),
        widget=forms.Select(attrs={'type': 'time', 'class': 'form-control height_element','id':'time_of_appointment', 'placeholder': 'hh:mm'})
    )

    doctor = forms.ModelChoiceField(
        queryset=Doctor.objects.filter(is_active=True),
        empty_label="Select Doctor"
    )

    patient_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'autocomplete': 'off', 'placeholder': 'Patient Name'}))
    age = forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(150)], widget=forms.TextInput(attrs={'autocomplete': 'off', 'placeholder': 'Age'}))

    mobile_number = forms.CharField( max_length=15, validators=[validate_mobile_number],widget=forms.TextInput(attrs={'autocomplete': 'off', 'placeholder': 'Mobile Number'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'autocomplete': 'off', 'placeholder': 'Your Message', 'rows': '4','class':'form-control'}), required=False)
    
    class Meta:
        model = Appointment
        fields = ['patient_name', 'age', 'mobile_number', 'date_of_appointment','time_of_appointment', 'doctor', 'message']
    
    def clean(self):
        cleaned_data = super().clean()

        doctor = cleaned_data.get('doctor')
        appointment_date = cleaned_data.get('date_of_appointment')
        appointment_time = cleaned_data.get('time_of_appointment')

        if doctor and appointment_date and appointment_time:
            # Check if the doctor is available
            if not is_doctor_available(doctor, appointment_date, appointment_time):
                raise ValidationError('Doctor is not available at the specified date and time.')

        return cleaned_data
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize the doctor field widget to display doctor names
        
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['required'] = True
       
        # Customize the appearance of the date input field
        self.fields['date_of_appointment'].widget = forms.TextInput(attrs={'type': 'date', 'class': 'form-control height_element', 'required': True})
        self.fields['doctor'].widget.attrs['class'] = 'form-control height_element'
        self.fields['time_of_appointment'].widget.attrs['class'] = 'form-control height_element'
        self.fields['time_of_appointment'].widget.attrs['placeholder'] = 'hh:mm'
        self.fields['message'].widget.attrs['class'] = 'form-control'
 
        def clean_appointment_date(self):
            date_of_appointment = self.cleaned_data.get('date_of_appointment')

            # Validate that the date is not in the past (you can customize this validation)
            if date_of_appointment and date_of_appointment < timezone.now().date():
                raise forms.ValidationError("Appointment date must be in the future.")

            return date_of_appointment
        

class DoctorEnrollmentForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'specialization', 'bio', 'image']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['required'] = True
    
