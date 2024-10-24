
from django.shortcuts import render, redirect, get_object_or_404
from .models import Driver
from .forms import DriverForm, AssignVehicleForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required
def drivers_list(request):
    driver_list = Driver.objects.all()
    paginator = Paginator(driver_list, 10)
    
    page_number = request.GET.get('page')
    drivers = paginator.get_page(page_number)

    return render(request, 'drivers-list.html', {'drivers': drivers})

@login_required
def create_driver(request):
    if request.method == 'POST':
        form = DriverForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('driver-list')
    else:
        form = DriverForm()
    return render(request, 'create-driver.html', {'form': form})

@login_required
def update_driver(request, driver_id):
    driver = get_object_or_404(Driver, id=driver_id)
    if request.method == 'POST':
        form = DriverForm(request.POST, instance=driver)
        if form.is_valid():
            form.save()
            return redirect('driver-list')
    else:
        form = DriverForm(instance=driver)
    return render(request, 'update-driver.html', {'form': form})

@login_required
def delete_driver(request, driver_id):
    driver = get_object_or_404(Driver, id=driver_id)
    if request.method == 'POST':
        driver.delete()
        return redirect('driver-list')
    return render(request, 'delete-driver.html', {'driver': driver})

@login_required
def view_driver(request, driver_id):
    driver = get_object_or_404(Driver, id=driver_id)
    return render(request, 'view-driver.html', {'driver': driver})


@login_required
def assign_vehicle_to_driver(request, driver_id):
    driver = get_object_or_404(Driver, id=driver_id)

    if request.method == 'POST':
        form = AssignVehicleForm(request.POST, instance=driver)
        if form.is_valid():
            form.save()  
            return redirect('driver-list') 
    else:
        form = AssignVehicleForm(instance=driver)

    return render(request, 'assign-vehicle.html', {'form': form, 'driver': driver})