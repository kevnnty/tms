from django import forms
from .models import Route

class RouteForm(forms.ModelForm):
  class Meta:
    model = Route
    fields = '__all__'
    widgets = {
      'estimated_travel_time': forms.TimeInput(format='%H:%M:%S'),
    }
    labels = {
      'route_name': 'Route Name',
      'start_location': 'Start Location',
      'end_location': 'End Location',
      'estimated_travel_time': 'Estimated Travel Time',
      'distance': 'Distance (km)',
      'vehicles': 'Assign Vehicles',
    }