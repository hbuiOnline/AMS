from django.shortcuts import render,redirect 
from django.http import HttpResponse

# Create your views here.
from .models import *
from .forms import *

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

#Tables in appliacation
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

#Dynamic For Profile
def customer(request, pk):
    customer = Customer.objects.get(id=pk)

    appointments = customer.appointment_set.all()
    total_appmt = appointments.count()

    context = {'customer': customer, 'appointments': appointments, 'total_appmt': total_appmt}
    return render(request, 'app/customer.html', context)

def staff(request, pk):
    staff = Staff.objects.get(id=pk)

    appointments = staff.appointment_set.all()
    total_appmt = appointments.count()

    context = {'staff': staff, 'appointments': appointments, 'total_appmt': total_appmt}
    return render(request, 'app/staff.html', context)


def appointment(request, pk):
    appointment = Appointment.objects.get(id=pk)

    context = {'appointment': appointment}
    return render(request, 'app/appointment.html', context)


#CRUD
def createAppointment(request, pk):
    customer = Customer.objects.get(id=pk)
    form = AppointmentForm(initial={'customer': customer})

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(customer) #need to redirect to customer/pk page

    context = {'form': form, 'customer': customer}
    return render(request, 'app/appmt_form.html', context)


def deleteAppointment(request, pk):
    appointment = Appointment.objects.get(id=pk)
    if request.method == 'POST':
        appointment.delete()
        return redirect('/appointments') #for admin
        # return redirect(customer) #for customer

    context = {'appointment': appointment}
    return render(request, 'app/delete_appmt.html', context)

def updateAppointment(request, pk):
    appointment = Appointment.objects.get(id=pk)
    form = AppointmentForm(instance=appointment)
    # customer = Customer.objects.get(id=pk)

    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('/appointments') #sending back to customer page

    context = {'form': form}
    return render(request, 'app/appmt_form.html', context)

def statusUpdate(request, pk):
    appointment = Appointment.objects.get(id=pk)
    statusForm = StatusForm(instance=appointment)
    if request.method == 'POST':
        statusForm = StatusForm(request.POST, instance=appointment)
        if statusForm.is_valid():
            statusForm.save()
            return redirect(appointment)

    context = {'statusForm': statusForm, 'appointment': appointment}
    return render(request, 'app/check_in.html', context)



