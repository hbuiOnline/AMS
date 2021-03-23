from django.urls import path
from . import views

urlpatterns = [

    # Authentication
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('', views.home, name="home"),
    path('appointments/', views.appointments, name="appointments"),
    path('customers/', views.customers, name="customers"),
    path('staffs/', views.staffs, name="staffs"),

    # Details
    path('user/', views.userPage, name='user-page'),
    path('user/staff/', views.userStaffPage, name='user-staff'),
    path('account/customer', views.customerAccountSettings, name='customer_account'),
    path('account/staff', views.staffAccountSettings, name='staff_account'),
    path('customer/<str:pk>', views.customer, name="customer"),
    path('staff/<str:pk>', views.staff, name="staff"),
    path('appointment/<str:pk>', views.appointment, name="appointment"),

    # CRUD
    path('create_appmt/<str:pk>', views.createAppointment, name="create_appmt"),
    path('update_appmt/<str:pk>', views.updateAppointment, name="update_appmt"),
    path('delete_appmt/<str:pk>', views.deleteAppointment, name="delete_appmt"),

    # Status Update
    path('check_in/<str:pk>', views.statusUpdate, name="check_in"),
    # path('check_out/<str:pk>', views.statusUpdate, name="check_out"),






]
