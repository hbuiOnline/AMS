from django.forms import ModelForm
from django import forms

# Authentication
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  # import User model

from .models import *


# inherited the UserCreationForm, replicate it customer the field
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        # this will give the form of only these fields
        fields = ['username', 'email', 'password1', 'password2']


class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        # fields = '__all__'
        fields = ['customer', 'date', 'time', 'assigned', 'service', 'note']

        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control'}),
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


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }


class StaffForm(ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'
        exclude = ['user']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }
