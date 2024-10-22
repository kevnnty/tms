from django import forms
from .models import Vehicle
from drivers.models import Driver

class VehicleForm(forms.ModelForm):
  class Meta:
    model = Vehicle
    fields = '__all__'
    
    
class DriverAssignForm(forms.Form):
  driver = forms.ModelChoiceField(queryset=Driver.objects.filter(vehicle__isnull=True), label="Select Driver")    