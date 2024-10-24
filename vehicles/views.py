from django.shortcuts import render, redirect, get_object_or_404
from .models import Vehicle
from .forms import VehicleForm, DriverAssignForm, RouteAssignForm;
from drivers.models import Driver
from django.contrib.auth.decorators import login_required


@login_required
def vehicles_list(request):
  vehicles = Vehicle.objects.all()
  return render(request, 'vehicles-list.html', {'vehicles': vehicles })


@login_required    
def create_vehicle(request):
  if request.method == 'POST':
    form = VehicleForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('vehicle-list')
  else:
    form = VehicleForm()
      
  return render(request, 'create-vehicle.html', {'form': form})


@login_required
def update_vehicle(request, vehicle_id):
  vehicle = get_object_or_404(Vehicle, id=vehicle_id)
  if request.method == 'POST':
    form = VehicleForm(request.POST, instance=vehicle)
    if form.is_valid():
      form.save() 
      return redirect('vehicle-list')            
  else:
      form = VehicleForm(instance=vehicle)

  return render(request, 'update-vehicle.html', {'form': form, 'vehicle': vehicle})


@login_required
def delete_vehicle(request, vehicle_id):
  vehicle = get_object_or_404(Vehicle, id=vehicle_id)
  
  if request.method == 'POST':
    vehicle.delete()
    return redirect('vehicle-list')
  
  return render(request, 'delete-vehicle.html', {'vehicle': vehicle})

@login_required
def assign_driver_to_vehicle(request, vehicle_id):
  vehicle = get_object_or_404(Vehicle, id=vehicle_id)
  
  if request.method == 'POST':
    form = DriverAssignForm(request.POST)
    if form.is_valid():
      driver = form.cleaned_data['driver']
      driver.vehicle = vehicle
      driver.save()
      return redirect('view-vehicle', vehicle.id)
  else:
      form = DriverAssignForm()

  return render(request, 'assign-driver.html', {'vehicle': vehicle, 'form': form })


@login_required
def view_vehicle(request, vehicle_id):
  vehicle = get_object_or_404(Vehicle, id=vehicle_id)
  driver = Driver.objects.filter(vehicle=vehicle).first()
  return render(request, 'view-vehicle.html', {'vehicle': vehicle, 'driver': driver})


@login_required
def assign_route(request, vehicle_id):
  vehicle = get_object_or_404(Vehicle, id=vehicle_id)
   
  if request.method == 'POST':
    form = RouteAssignForm(request.POST)
    if form.is_valid():
      route = form.cleaned_data['route']
      vehicle.route = route
      vehicle.save()
      return redirect('vehicle-list')
  else:
      form = RouteAssignForm()

  return render(request, 'assign-route.html', {'vehicle': vehicle, 'form': form })