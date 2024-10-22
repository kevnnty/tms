from django.shortcuts import render, redirect, get_object_or_404
from .models import Vehicle
from .forms import VehicleForm, DriverAssignForm;
from drivers.models import Driver
from django.db.models import Q

def list_vehicles(request):
  query = request.GET.get('search', '')
  vehicles = Vehicle.objects.filter(
    Q(license_plate__icontains=query) | 
    Q(model__icontains=query) | 
    Q(status__iexact=query)
  )
  return render(request, 'vehicles/vehicles-list.html', {'vehicles': vehicles, 'query': query})

    
def create_vehicle(request):
  if request.method == 'POST':
    form = VehicleForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('vehicle-list')
  else:
    form = VehicleForm()
      
  return render(request, 'vehicles/create-vehicle.html', {'form': form})


def update_vehicle(request, vehicle_id):
  vehicle = get_object_or_404(Vehicle, id=vehicle_id)
  if request.method == 'POST':
    form = VehicleForm(request.POST, instance=vehicle)
    if form.is_valid():
      form.save() 
      return redirect('vehicle-list')            
  else:
      form = VehicleForm(instance=vehicle)

  return render(request, 'vehicles/update-vehicle.html', {'form': form})


def delete_vehicle(request, vehicle_id):
  vehicle = get_object_or_404(Vehicle, id=vehicle_id)
  
  if request.method == 'POST':
    vehicle.delete()
    return redirect('vehicle-list')
  
  return render(request, 'vehicles/delete-vehicle.html', {'vehicle': vehicle})


def assign_driver_to_vehicle(request, vehicle_id):
  vehicle = get_object_or_404(Vehicle, id=vehicle_id)
  
  if request.method == 'POST':
    form = DriverAssignForm(request.POST)
    if form.is_valid():
      driver = form.cleaned_data['driver']
      driver.vehicle = vehicle
      driver.save()
      return redirect('vehicle-list')
  else:
      form = DriverAssignForm()

  return render(request, 'vehicles/assign-driver.html', {'vehicle': vehicle, 'form': form })

def view_vehicle(request, vehicle_id):
  vehicle = get_object_or_404(Vehicle, id=vehicle_id)
  driver = Driver.objects.filter(vehicle=vehicle).first()
  return render(request, 'vehicles/view-vehicle.html', {'vehicle': vehicle, 'driver': driver})



