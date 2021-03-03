from django.db import models

# Create your models here.
# Create class that represent our database

class Customer(models.Model):
    name = models.CharField(max_length=200, null=True) #null=true will let insert into table without filling out all the fields
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True) #Auto create/insert time whenever there is created instance in the Customer table

    def __str__(self):
        return self.name

class Staff(models.Model):
    name = models.CharField(max_length=200, null=True) #null=true will let insert into table without filling out all the fields
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True) #Auto create/insert time whenever there is created instance in the Customer table

    def __str__(self):
        return self.name

class Service(models.Model):
    description = models.CharField(max_length=200, null=True)
    cost = models.FloatField(null=True)

    def __str__(self):
        return self.description

class Appointment(models.Model):
    STATUS = ( #tuple
        ('Scheduled', 'Scheduled'),
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
    )

    # datetime = 
    status = models.CharField(max_length=200, null=True, choices=STATUS, default="Scheduled")
    assigned = models.ForeignKey(Staff, null=True, on_delete=models.SET_NULL)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    service = models.ForeignKey(Service, null=True, on_delete=models.SET_NULL)
    note = models.TextField(null=True, blank=True, default="None")

    def __str__(self):
        return self.customer.name