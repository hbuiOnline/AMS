from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('appointments/', views.appointments, name="appointments"),
    path('customers/', views.customers, name="customers"),
    path('staffs/', views.staffs, name="staffs"),

    path('customer/<str:pk>', views.customer, name="customer"),
    path('staff/<str:pk>', views.staff, name="staff"),
    path('appointment/<str:pk>', views.appointment, name="appointment"),




]