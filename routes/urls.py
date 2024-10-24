from django.urls import path
from .views import add_route, delete_route, edit_route, routes_list, route_details, assign_vehicles_to_route


urlpatterns = [
  path('', routes_list, name='routes-list'),
  path('add/', add_route, name='add-route'), 
  path('<int:route_id>/', route_details, name='route-details'),
  path('edit/<int:route_id>/', edit_route, name='edit-route'),
  path('delete/<int:route_id>/', delete_route, name='delete-route'),
  path('<int:route_id>/assign-vehicles', assign_vehicles_to_route, name='assign-vehicles-to-route') 
]