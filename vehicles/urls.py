# transport_management/apps/vehicles/urls.py

from django.urls import path
from .views import vehicle_list, vehicle_create, render_vehicle_list, render_vehicle_create

urlpatterns = [
    path('api/vehicles/', vehicle_list, name='vehicle-list'),  # API endpoint to list vehicles
    path('api/vehicles/create/', vehicle_create, name='vehicle-create'),  # API endpoint to create a vehicle
    path('list/', render_vehicle_list, name='vehicle-list-template'),  # Render template for vehicle list
    path('create/', render_vehicle_create, name='vehicle-create-template'),  # Render template for vehicle creation
]
