from django.urls import path
from .views import ( create_driver, delete_driver, drivers_list, update_driver, view_driver, assign_vehicle_to_driver )

urlpatterns = [
  path('', drivers_list, name='driver-list'),
  path('create/', create_driver, name='create-driver'),
  path('update/<int:driver_id>/', update_driver, name='update-driver'),
  path('delete/<int:driver_id>/', delete_driver, name='delete-driver'),
  path('<int:driver_id>/', view_driver, name='view-driver'),
  path('assign/<int:driver_id>/', assign_vehicle_to_driver, name='assign-vehicle-to-driver'),
]
