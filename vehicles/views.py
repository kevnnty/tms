
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Vehicle
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt  # Disable CSRF verification for this example (use cautiously in production)
def vehicle_list(request):
    if request.method == 'GET':
        vehicles = Vehicle.objects.all().values()  # Use .values() to get dict-like objects
        return JsonResponse(list(vehicles), safe=False)  # Return as JSON response
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)

@csrf_exempt
def vehicle_create(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # Get JSON data from the request body
            make = data.get('make')
            model = data.get('model')
            license_plate = data.get('license_plate')
            capacity = data.get('capacity')
            status = data.get('status')

            # Create and save the vehicle
            vehicle = Vehicle(make=make, model=model, license_plate=license_plate, capacity=capacity, status=status)
            vehicle.save()

            return JsonResponse({'id': vehicle.id, 'make': vehicle.make, 'model': vehicle.model}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)

# Render templates for listing and creating vehicles
def render_vehicle_list(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'vehicles/vehicle_list.html', {'vehicles': vehicles})

def render_vehicle_create(request):
    return render(request, 'vehicles/vehicle_create.html')
