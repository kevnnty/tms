from django.urls import path
from .views import list_vehicles, create_vehicle, delete_vehicle, get_single_vehicle, update_vehicle

urlpatterns = [
    path('', list_vehicles, name='vehicle-list'), 
    path('id/', get_single_vehicle, name='get-single-vehicle'), 
    path('create/', create_vehicle, name='create-vehicle'),  
    path('update/', update_vehicle , name='update-vehicle'),  
    path('delete/', delete_vehicle, name='delete-vehicle'),  
]
