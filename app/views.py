from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from django.contrib import messages

# Create your views here.
from .models import *
from .forms import *
from .decorators import unauthenticated_user, allowed_users, admin_only


@unauthenticated_user
def register(request):
    return render(request, 'app/register.html')


@unauthenticated_user
def registerCustomer(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)  # using the form in forms.py
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')  # get the username

            # This will let create group on registration
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            Customer.objects.create(
                user=user,  # create user associated with customer
                name=request.POST.get('first_name') + \
                " " + request.POST.get('last_name'),
            )

            messages.success(request, 'Account was created for ' + username)
            return redirect('login')

    context = {'form': form}
    return render(request, 'app/registerCustomer.html', context)


@unauthenticated_user
def registerStaff(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)  # using the form in forms.py
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')  # get the username

            # This will let create group on registration
            group = Group.objects.get(name='staff')
            user.groups.add(group)
            Staff.objects.create(
                user=user,  # create user associated with customer
                name=request.POST.get('first_name') + \
                " " + request.POST.get('last_name'),
            )

            messages.success(request, 'Account was created for ' + username)
            return redirect('login')

    context = {'form': form}
    return render(request, 'app/registerStaff.html', context)


@unauthenticated_user
def loginPage(request):
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
    pending = appointments.filter(status="Pending").count()
    scheduled = appointments.filter(status="Scheduled").count()
    completed = appointments.filter(status="Completed").count()

    # services = []
    # for i in range(1, 5):
    #     services.append(appointments.filter(service=i).count())
    service1 = appointments.filter(service=1).count()
    service2 = appointments.filter(service=2).count()
    service3 = appointments.filter(service=3).count()
    service4 = appointments.filter(service=4).count()
    service5 = appointments.filter(service=5).count()

    context = {'total_appmt': total_appmt,
               'total_staff': total_staff,
               'total_customers': total_customers,
               'pending': pending,
               'scheduled': scheduled,
               'completed': completed,
               'service1': service1,
               'service2': service2,
               'service3': service3,
               'service4': service4,
               'service5': service5,
               }

    return render(request, 'app/dashboard.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def userPage(request):
    appointments = request.user.customer.appointment_set.all()

    group = request.user.groups.all()[0].name

    total_appmt = appointments.count()
    scheduled = appointments.filter(status='Scheduled').count()
    completed = appointments.filter(status='Completed').count()

    context = {'appointments': appointments, 'total_appmt': total_appmt,
               'scheduled': scheduled, 'completed': completed, 'group': group}
    return render(request, 'app/user.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['staff'])
def userStaffPage(request):
    appointments = request.user.staff.appointment_set.all()

    group = request.user.groups.all()[0].name

    total_appmt = appointments.count()
    scheduled = appointments.filter(status='Scheduled').count()
    completed = appointments.filter(status='Completed').count()

    context = {'appointments': appointments, 'total_appmt': total_appmt,
               'scheduled': scheduled, 'completed': completed, 'group': group}
    return render(request, 'app/user-staff.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def customerAccountSettings(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)
    group = request.user.groups.all()[0].name

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()

    context = {'form': form, 'customer': customer, 'group': group}
    return render(request, 'app/customerAccount.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['staff'])
def staffAccountSettings(request):
    staff = request.user.staff
    form = StaffForm(instance=staff)
    group = request.user.groups.all()[0].name

    if request.method == 'POST':
        form = StaffForm(request.POST, request.FILES, instance=staff)
        if form.is_valid():
            form.save()

    context = {'form': form, 'staff': staff, 'group': group}
    return render(request, 'app/staffAccount.html', context)

#Tables in application


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
@allowed_users(allowed_roles=['admin', 'customer'])
def customer(request, pk):
    customer = Customer.objects.get(id=pk)

    appointments = customer.appointment_set.all()
    total_appmt = appointments.count()

    context = {'customer': customer,
               'appointments': appointments, 'total_appmt': total_appmt}
    return render(request, 'app/customer.html', context)


# if user is not login, send it to the login page
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'staff'])
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
    group = request.user.groups.all()[0].name

    context = {'appointment': appointment, 'group': group}
    return render(request, 'app/appointment.html', context)


# CRUD
# if user is not login, send it to the login page
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'customer'])
def createAppointment(request, pk):
    customer = Customer.objects.get(id=pk)
    form = AppointmentForm(initial={'customer': customer})
    group = request.user.groups.all()[0].name

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            if request.user.is_staff:
                # for admin to redirect to customer/pk page
                return redirect(customer)
            else:
                return redirect('home')  # for customer user

    context = {'form': form, 'customer': customer, 'group': group}
    return render(request, 'app/appmt_form.html', context)


# if user is not login, send it to the login page
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'customer'])
def deleteAppointment(request, pk):
    appointment = Appointment.objects.get(id=pk)
    group = request.user.groups.all()[0].name
    if request.method == 'POST':
        appointment.delete()
        if request.user.is_staff:
            return redirect('/appointments')  # for admin
        else:
            return redirect('user-page')  # for customer user can delete

    context = {'appointment': appointment, 'group': group}
    return render(request, 'app/delete_appmt.html', context)


# if user is not login, send it to the login page
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateAppointment(request, pk):
    appointment = Appointment.objects.get(id=pk)
    form = AppointmentForm(instance=appointment)
    group = request.user.groups.all()[0].name

    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('/appointments')

    context = {'form': form, 'group': group}
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


def unauthorizedPage(request):
    return render(request, 'app/unauthorized.html')
