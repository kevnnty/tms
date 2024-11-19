from django.shortcuts import render
from vehicles.models import Vehicle
from routes.models import Route
from drivers.models import Driver

import json

# Analytics view to render the dashboard with graphs
def analytics_dashboard(request):
    # Fetch data for routes, vehicles, and drivers
    routes = Route.objects.all()
    vehicles = Vehicle.objects.all()
    drivers = Driver.objects.all()

    vehicle_usage_data = {
        'vehicles': [vehicle.license_plate for vehicle in vehicles],
        'total_trips': [vehicle.total_trips for vehicle in vehicles],
        'total_distance': [vehicle.total_distance for vehicle in vehicles],
    }

    driver_earnings_data = {
        'drivers': [driver.name for driver in drivers],
        'total_earnings': [driver.total_earnings for driver in drivers],
        'total_trips': [driver.total_trips for driver in drivers],
    }

    context = {
        'vehicle_usage_data': vehicle_usage_data,
        'driver_earnings_data': driver_earnings_data,
    }

    return render(request, 'analytics.html', context)
