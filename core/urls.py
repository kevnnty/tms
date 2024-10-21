from django.urls import path
from .views import list_vehicles, create_vehicle, delete_vehicle, get_single_vehicle, update_vehicle

urlpatterns = [
    path('', list_vehicles, name='vehicle-list'), 
    path('vehicle/<int:vehicle_id>', get_single_vehicle, name='get-single-vehicle'), 
    path('vehicle/create/', create_vehicle, name='create-vehicle'),  
    path('vehicle/update/<int:vehicle_id>', update_vehicle , name='update-vehicle'),  
    path('vehicle/delete/<int:vehicle_id>', delete_vehicle, name='delete-vehicle'),  
]
