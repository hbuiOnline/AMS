from django.forms import ModelForm
from django import forms
from .models import *

class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        # fields = '__all__'
        fields = ['customer', 'date', 'time', 'assigned', 'service', 'note']

        widgets = {
            'date': forms.DateInput(attrs={'class':'form-control'}),
            'time': forms.Select(attrs={'class': 'form-control'}),
            'assigned': forms.Select(attrs={'class': 'form-control'}),
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'service': forms.Select(attrs={'class': 'form-control'}),
            'note': forms.TextInput(attrs={'class': 'form-control'}),
        }

        