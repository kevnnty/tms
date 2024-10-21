from django.db import models

# Create your models here.
class Vehicle(models.Model):
    NUMBER_PLATE_MAX_LENGTH = 15
    MODEL_MAX_LENGTH = 50

    license_plate = models.CharField(max_length=NUMBER_PLATE_MAX_LENGTH, unique=True)
    model = models.CharField(max_length=MODEL_MAX_LENGTH)
    capacity = models.IntegerField()
    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('inactive', 'Inactive')])


class Schedule(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()


class Driver(models.Model):
    name = models.CharField(max_length=100)
    license_number = models.CharField(max_length=50, unique=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True, blank=True)


class Route(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    start_location = models.CharField(max_length=100)
    end_location = models.CharField(max_length=100)
