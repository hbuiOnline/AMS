from django.forms import ModelForm
from django import forms

#Authentication
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User #import User model

from .models import *

class CreateUserForm(UserCreationForm): #inherited the UserCreationForm, replicate it customer the field
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2'] #this will give the form of only these fields

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

class StatusForm(ModelForm):
    class Meta:
        model = Appointment
        error_css_class = "alert alert-danger"
        fields = ['status']
        # widgets = {'status': forms.HiddenInput()}
        