from django import forms
from .models import Vehicle, Driver;

class VehicleForm(forms.ModelForm):
  class Meta:
    model = Vehicle
    fields = '__all__'


class DriverForm(forms.ModelForm):
  class Meta:
    model = Driver
    fields = '__all__'


class AssignVehicleForm(forms.ModelForm):
  class Meta:
    model = Driver
    fields = ['vehicle']

class DriverAssignForm(forms.Form):
    driver = forms.ModelChoiceField(queryset=Driver.objects.filter(vehicle__isnull=True), label="Select Driver")