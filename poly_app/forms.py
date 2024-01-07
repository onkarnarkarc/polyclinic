# clinic/forms.py
from django import forms
from .models import Appointment, Doctor, VisitType
from datetime import timezone
from django.core.exceptions import ValidationError
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

class DateInput(forms.DateInput):
    input_type = 'date'

class VisitTypeForm(forms.ModelForm):
    class Meta:
        model = VisitType
        fields = ['name']


class AppointmentEntryForm(forms.ModelForm):
    time_of_appointment = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time', 'class': 'form-control height_element','id':'time_of_appointment', 'placeholder': 'hh:mm'})
    )

    doctor = forms.ModelChoiceField(
        queryset=Doctor.objects.filter(is_active=True),
        empty_label="Select Doctor"
    )

    patient_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'autocomplete': 'off', 'placeholder': 'Patient Name'}))
    age = forms.IntegerField( widget=forms.TextInput(attrs={'autocomplete': 'off', 'placeholder': 'Age'}))

    mobile_number = forms.CharField( max_length=15, validators=[validate_mobile_number],widget=forms.TextInput(attrs={'autocomplete': 'off', 'placeholder': 'Mobile Number'}))

    class Meta:
        model = Appointment
        
        fields = ['patient_name', 'age', 'mobile_number', 'date_of_appointment','time_of_appointment', 'doctor', 'message']
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
    
