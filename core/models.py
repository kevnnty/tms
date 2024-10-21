from django.db import models

# Create your models here.
class Vehicle(models.Model):
    NUMBER_PLATE_MAX_LENGTH = 15
    MODEL_MAX_LENGTH = 50

    license_plate = models.CharField(max_length=NUMBER_PLATE_MAX_LENGTH, unique=True)
    model = models.CharField(max_length=MODEL_MAX_LENGTH)
    capacity = models.IntegerField()
    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('inactive', 'Inactive')])
