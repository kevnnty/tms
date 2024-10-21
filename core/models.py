from django.db import models

# Create your models here.

class Vehicle(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    license_plate = models.CharField(max_length=20, unique=True)
    capacity = models.IntegerField()
    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('inactive', 'Inactive')])
