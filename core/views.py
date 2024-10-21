from django.shortcuts import render, redirect, get_object_or_404
from .models import Vehicle, Driver
from .forms import VehicleForm, DriverForm;

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


def view_vehicle(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)
    return render(request, 'vehicles/view-vehicle.html', {'vehicle': vehicle})


def list_drivers(request):
    drivers = Driver.objects.all()
    return render(request, 'drivers/drivers-list.html', {'drivers': drivers})

def create_driver(request):
    if request.method == 'POST':
        form = DriverForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('driver-list')
    else:
        form = DriverForm()
    return render(request, 'drivers/create-driver.html', {'form': form})

def update_driver(request, driver_id):
    driver = get_object_or_404(Driver, id=driver_id)
    if request.method == 'POST':
        form = DriverForm(request.POST, instance=driver)
        if form.is_valid():
            form.save()
            return redirect('driver-list')
    else:
        form = DriverForm(instance=driver)
    return render(request, 'drivers/update-driver.html', {'form': form})

def delete_driver(request, driver_id):
    driver = get_object_or_404(Driver, id=driver_id)
    if request.method == 'POST':
        driver.delete()
        return redirect('driver-list')
    return render(request, 'drivers/delete-driver.html', {'driver': driver})

def view_driver(request, driver_id):
    driver = get_object_or_404(Driver, id=driver_id)
    return render(request, 'drivers/view-driver.html', {'driver': driver})