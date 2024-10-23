from django.db import models

# Create your models here.

class Route(models.Model):
  start_location = models.CharField(max_length=100)
  end_location = models.CharField(max_length=100)
  estimated_travel_time = models.DurationField()
  distance = models.FloatField()

  def __str__(self):
    return f"{self.start_location} - {self.end_location}"