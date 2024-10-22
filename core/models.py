from django.db import models

# Create your models here.
class Vehicle(models.Model):
    NUMBER_PLATE_MAX_LENGTH = 15
    MODEL_MAX_LENGTH = 50

    license_plate = models.CharField(max_length=NUMBER_PLATE_MAX_LENGTH, unique=True)
    model = models.CharField(max_length=MODEL_MAX_LENGTH)
    capacity = models.IntegerField()
    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('inactive', 'Inactive')])
    
    def __str__(self):
        return f"{self.license_plate} - {self.model}"


class Schedule(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    
    def __str__(self):
        return f"{self.vehicle.license_plate} - {self.departure_time} - {self.arrival_time}"


class Driver(models.Model):
    name = models.CharField(max_length=100)
    license_number = models.CharField(max_length=50, unique=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f"{self.name} - {self.license_number}"


class Route(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    start_location = models.CharField(max_length=100)
    end_location = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.vehicle.license_plate} - {self.start_location} - {self.end_location}"
