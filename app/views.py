from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import *

def home(request):

    appointments = Appointment.objects.all()
    staffs = Staff.objects.all()
    customers = Customer.objects.all()

    total_appmt = appointments.count()
    total_staff = staffs.count()
    total_customers = customers.count()

    context = {'total_appmt': total_appmt,
               'total_staff': total_staff,
               'total_customers': total_customers,
        }

    return render(request, 'app/dashboard.html', context)

def appointments(request):
    appointments = Appointment.objects.all()

    context = {'appointments': appointments,}
    return render(request, 'app/appointments.html', context)

def customers(request):
    customers = Customer.objects.all()

    context = {'customers': customers}
    return render(request, 'app/customers.html', context)

def staffs(request):
    staffs = Staff.objects.all()

    context = {'staffs': staffs}
    return render(request, 'app/staffs.html', context)



