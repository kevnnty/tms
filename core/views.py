from django.http import HttpResponse
from django.shortcuts import render
from .models import Vehicle

def list_vehicles(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'vehicles_list.html', {'vehicles': vehicles})
    
    
def create_vehicle(request):
    if request.method == 'POST':
        return HttpResponse("Creating vehicle endpoint!")
    else: 
        return HttpResponse("Unsupported method!")    


def update_vehicle(request):
    return render(request, 'update_vehicle.html')


def delete_vehicle(request):
    return render(request, 'delete_vehicle.html')


def get_single_vehicle(request):
    return render(request, 'get_single_vehicle.html')