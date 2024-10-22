
from django.shortcuts import render, redirect, get_object_or_404
from .models import Driver
from .forms import DriverForm, AssignVehicleForm

from django.db.models import Q


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


def assign_vehicle_to_driver(request, driver_id):
    driver = get_object_or_404(Driver, id=driver_id)

    if request.method == 'POST':
        form = AssignVehicleForm(request.POST, instance=driver)
        if form.is_valid():
            form.save()  
            return redirect('driver-list') 
    else:
        form = AssignVehicleForm(instance=driver)

    return render(request, 'drivers/assign-vehicle.html', {'form': form, 'driver': driver})