# forms.py
from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['user', 'doctor', 'date', 'time']
        # Add any additional form customization as needed
