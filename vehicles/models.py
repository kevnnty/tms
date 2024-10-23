from django.db import models
from routes.models import Route

class Vehicle(models.Model):
    NUMBER_PLATE_MAX_LENGTH = 15
    MODEL_MAX_LENGTH = 50
    CATEGORY_CHOICES = [
        ('taxi', 'Taxi'),
        ('cab', 'Cab'),
        ('bus', 'Bus'),
        ('coaster', 'Coaster (Minibus)'),
        ('coach', 'Coach'),
        ('bike', 'Bike'),
        ('van', 'Van'),
    ]

    license_plate = models.CharField(max_length=NUMBER_PLATE_MAX_LENGTH, unique=True)
    model = models.CharField(max_length=MODEL_MAX_LENGTH)
    capacity = models.IntegerField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default=CATEGORY_CHOICES[0])
    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('inactive', 'Inactive')])
    route = models.ForeignKey(Route, on_delete=models.SET_NULL, null=True, blank=True, related_name='vehicles')

    def __str__(self):
        return f"{self.license_plate} - {self.model}"