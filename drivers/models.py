from django.db import models
from vehicles.models import Vehicle

class Driver(models.Model):
  name = models.CharField(max_length=100)
  license_number = models.CharField(max_length=50, unique=True)
  vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True, blank=True)  
  total_trips = models.PositiveIntegerField(default=0)
  total_earnings = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)

  
  def __str__(self):
    return f"{self.name} - {self.license_number}"