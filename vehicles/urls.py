from django.urls import path
from .views import ( vehicles_list, create_vehicle, delete_vehicle, view_vehicle, update_vehicle, assign_driver_to_vehicle, assign_route)

urlpatterns = [
  path('', vehicles_list, name='vehicle-list'), 
  path('<int:vehicle_id>', view_vehicle, name='view-vehicle'), 
  path('create/', create_vehicle, name='create-vehicle'),  
  path('update/<int:vehicle_id>', update_vehicle , name='update-vehicle'),  
  path('delete/<int:vehicle_id>', delete_vehicle, name='delete-vehicle'),  
  path('<int:vehicle_id>/assign-driver/', assign_driver_to_vehicle, name='assign-driver-to-vehicle'),  
  path('<int:vehicle_id>/assign-route', assign_route, name='assign-route-to-vehicle'),

]