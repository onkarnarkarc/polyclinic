# clinic/forms.py
from django import forms
from .models import Appointment, Doctor, VisitType
from datetime import timezone
class DateInput(forms.DateInput):
    input_type = 'date'

class VisitTypeForm(forms.ModelForm):
    class Meta:
        model = VisitType
        fields = ['name']


class AppointmentEntryForm(forms.ModelForm):
    time_of_appointment = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time', 'class': 'form-control','id':'date'})
    )

    doctor = forms.ModelChoiceField(
        queryset=Doctor.objects.filter(is_active=True),
        empty_label="Select Doctor",
        widget=forms.Select(attrs={'class': 'form-control', 'required': True})
    )

    patient_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'autocomplete': 'off'}))
    mobile_number = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'autocomplete': 'off'}))
    class Meta:
        model = Appointment
        
        fields = ['patient_name', 'age', 'mobile_number', 'date_of_appointment','time_of_appointment', 'doctor']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize the doctor field widget to display doctor names
        # self.fields['doctor'].widget = forms.Select(choices=Doctor.objects.values_list('id', 'name'))
        
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['required'] = True
       
        # Customize the appearance of the date input field
        self.fields['date_of_appointment'].widget = forms.TextInput(attrs={'type': 'date', 'class': 'form-control', 'required': True})

        # self.fields['doctor'].widget = forms.TextInput(attrs={'type': 'date', 'class': 'form-control', 'required': True})
        # self.fields['time_of_appointment'] = forms.TimeField(attrs={'type': 'date', 'class': 'form-control', 'required': True})
         
        def clean_appointment_date(self):
            date_of_appointment = self.cleaned_data.get('date_of_appointment')

            # Validate that the date is not in the past (you can customize this validation)
            if date_of_appointment and date_of_appointment < timezone.now().date():
                raise forms.ValidationError("Appointment date must be in the future.")

            return date_of_appointment
        # self.fields['doctor'] = forms.ModelChoiceField(
        #     queryset=Doctor.objects.filter(is_active= True).values_list('id', 'name'),
        #     empty_label="Select Doctor",
        #     widget=forms.Select(attrs={'class': 'form-control', 'required': True})
        # )

class DoctorEnrollmentForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'specialization', 'bio', 'image']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['required'] = True
    
