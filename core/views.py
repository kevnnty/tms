from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Vehicle
from .forms import VehicleForm;

def list_vehicles(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'vehicles/vehicles-list.html', {'vehicles': vehicles})
    
    
def create_vehicle(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()  # This will create and save a new vehicle in the database
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


def get_single_vehicle(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)
    return render(request, 'vehicles/get-single-vehicle.html', {'vehicle': vehicle})
