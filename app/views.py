from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages

# Create your views here.
from .models import *
from .forms import *
from .decorators import unauthenticated_user, allowed_users, admin_only


@unauthenticated_user
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)  # using the form in forms.py
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')  # get the username
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')

        context = {'form': form}
        return render(request, 'app/register.html', context)


@unauthenticated_user
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            # grab the value of these fields
            username = request.POST.get('username')
            # these two are from the name= in HTML template
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.warning(request, 'Username OR password is Incorrect')

        context = {}
        return render(request, 'app/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def userPage(request):
    context = {}
    return render(request, 'app/user.html', context)


# if user is not login, send it to the login page
@login_required(login_url='login')
@admin_only
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


# if user is not login, send it to the login page
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def appointments(request):
    appointments = Appointment.objects.all()
    context = {'appointments': appointments, }
    return render(request, 'app/appointments.html', context)


# if user is not login, send it to the login page
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customers(request):
    customers = Customer.objects.all()
    context = {'customers': customers}
    return render(request, 'app/customers.html', context)


# if user is not login, send it to the login page
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def staffs(request):
    staffs = Staff.objects.all()
    context = {'staffs': staffs}
    return render(request, 'app/staffs.html', context)

# Dynamic For Profile


# if user is not login, send it to the login page
@login_required(login_url='login')
def customer(request, pk):
    customer = Customer.objects.get(id=pk)

    appointments = customer.appointment_set.all()
    total_appmt = appointments.count()

    context = {'customer': customer,
               'appointments': appointments, 'total_appmt': total_appmt}
    return render(request, 'app/customer.html', context)


# if user is not login, send it to the login page
@login_required(login_url='login')
def staff(request, pk):
    staff = Staff.objects.get(id=pk)

    appointments = staff.appointment_set.all()
    total_appmt = appointments.count()

    context = {'staff': staff, 'appointments': appointments,
               'total_appmt': total_appmt}
    return render(request, 'app/staff.html', context)


# if user is not login, send it to the login page
@login_required(login_url='login')
def appointment(request, pk):
    appointment = Appointment.objects.get(id=pk)

    context = {'appointment': appointment}
    return render(request, 'app/appointment.html', context)


# CRUD
# if user is not login, send it to the login page
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createAppointment(request, pk):
    customer = Customer.objects.get(id=pk)
    form = AppointmentForm(initial={'customer': customer})

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(customer)  # need to redirect to customer/pk page

    context = {'form': form, 'customer': customer}
    return render(request, 'app/appmt_form.html', context)


# if user is not login, send it to the login page
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteAppointment(request, pk):
    appointment = Appointment.objects.get(id=pk)
    if request.method == 'POST':
        appointment.delete()
        return redirect('/appointments')  # for admin
        # return redirect(customer) #for customer

    context = {'appointment': appointment}
    return render(request, 'app/delete_appmt.html', context)


# if user is not login, send it to the login page
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateAppointment(request, pk):
    appointment = Appointment.objects.get(id=pk)
    form = AppointmentForm(instance=appointment)
    # customer = Customer.objects.get(id=pk)

    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('/appointments')  # sending back to customer page

    context = {'form': form}
    return render(request, 'app/appmt_form.html', context)


# if user is not login, send it to the login page
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
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
