from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date

# Create your models here.
# Create class that represent our database


class Customer(models.Model):
    # when user us deleted, we will delete that relationship to the customers
    # user only have one customer, and a customer only have one user
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    # null=true will let insert into table without filling out all the fields
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(
        default="default-profile.png", null=True, blank=True)
    # Auto create/insert time whenever there is created instance in the Customer table, auto_now: for update, auto_now_add: for create
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/customer/%i" % self.id


class Staff(models.Model):
    # null=true will let insert into table without filling out all the fields
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    # Auto create/insert time whenever there is created instance in the Customer table
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Service(models.Model):
    description = models.CharField(max_length=200, null=True)
    cost = models.FloatField(null=True)

    def __str__(self):
        return self.description


class Appointment(models.Model):
    STATUS = (  # tuple
        ('Scheduled', 'Scheduled'),
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
    )

    TIME = (
        ('9:00 AM', '9:00 AM'),
        ('10:00 AM', '10:00 AM'),
        ('11:00 AM', '11:00 AM'),
        ('12:00 PM', '12:00 PM'),
        ('1:00 PM', '1:00 PM'),
        ('2:00 PM', '2:00 PM'),
        ('3:00 PM', '3:00 PM'),
        ('4:00 PM', '4:00 PM'),
    )

    date_created = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    time = models.CharField(max_length=10, choices=TIME)
    assigned = models.ForeignKey(Staff, null=True, on_delete=models.SET_NULL)
    customer = models.ForeignKey(
        Customer, null=True, on_delete=models.SET_NULL)
    service = models.ForeignKey(Service, null=True, on_delete=models.SET_NULL)
    status = models.CharField(
        max_length=200, null=True, choices=STATUS, default="Scheduled")
    note = models.TextField(null=True, blank=True, default="None")

    def __str__(self):
        return self.customer.name

    def get_absolute_url(self):
        return "/appointment/%i" % self.id
