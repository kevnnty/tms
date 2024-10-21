from django.urls import path
from .views import ( list_vehicles, create_vehicle, delete_vehicle, view_vehicle, update_vehicle,create_driver, delete_driver, list_drivers, update_driver, view_driver)

urlpatterns = [
    path('', list_vehicles, name='vehicle-list'), 
    path('vehicle/<int:vehicle_id>', view_vehicle, name='view-vehicle'), 
    path('vehicle/create/', create_vehicle, name='create-vehicle'),  
    path('vehicle/update/<int:vehicle_id>', update_vehicle , name='update-vehicle'),  
    path('vehicle/delete/<int:vehicle_id>', delete_vehicle, name='delete-vehicle'),  
    
    path('drivers/', list_drivers, name='driver-list'),
    path('drivers/create/', create_driver, name='create-driver'),
    path('drivers/update/<int:driver_id>/', update_driver, name='update-driver'),
    path('drivers/delete/<int:driver_id>/', delete_driver, name='delete-driver'),
    path('drivers/<int:driver_id>/', view_driver, name='view-driver'),
]
