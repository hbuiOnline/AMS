from django.urls import path

from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [

    # Authentication
    path('register/', views.register, name='register'),
    path('register/customer', views.registerCustomer, name='registerCustomer'),
    path('register/staff', views.registerStaff, name='registerStaff'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    # Password Recovery system
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="app/passwordRecovery/password_reset.html"),
         name="reset_password"),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="app/passwordRecovery/password_reset_sent.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>//', auth_views.PasswordResetConfirmView.as_view(template_name="app/passwordRecovery/password_reset_form.html"),
         name="password_reset_confirm"),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="app/passwordRecovery/password_reset_done.html"),
         name="password_reset_complete"),

    # 1 - Submit Email Form                       //PasswordResetView.as_view()
    # 2 - Email sent success message              //PasswordResetDoneView.as_view()
    # 3 - Link to password Reset form in email    //PasswordResetConfirmView.as_view()
    # 4 - Password successfully changed message   //PasswordResetCompleteView.as_view()

    # Data Tables
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
    path('check_in/<str:pk>', views.statusCheckIn, name="check_in"),
    path('check_out/<str:pk>', views.statusCheckOut, name="check_out"),

    # Unauthorized Page
    path('unauthorized/', views.unauthorizedPage, name="unauthorized"),






]
