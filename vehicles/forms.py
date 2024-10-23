from django import forms
from .models import Vehicle
from drivers.models import Driver
from routes.models import Route

class VehicleForm(forms.ModelForm):
  class Meta:
    model = Vehicle
    fields = '__all__'
    
    
class DriverAssignForm(forms.Form):
  driver = forms.ModelChoiceField(queryset=Driver.objects.filter(vehicle__isnull=True), label="Select Driver")
  

class RouteAssignForm(forms.Form):
  route = forms.ModelChoiceField(queryset=Route.objects.all(), empty_label="Select a Route")
