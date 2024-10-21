from django import forms
from .models import Vehicle, Driver;

class VehicleForm(forms.ModelForm):
  class Meta:
    model = Vehicle
    fields = '__all__'

# forms.py

class DriverForm(forms.ModelForm):
  class Meta:
      model = Driver
      fields = '__all__'
