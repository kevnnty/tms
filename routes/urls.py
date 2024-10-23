from django.urls import path
from .views import add_route, delete_route, edit_route, routes_list, route_detail


urlpatterns = [
  path('', routes_list, name='routes-list'),
  path('add/', add_route, name='add-route'), 
  path('<int:route_id>/', route_detail, name='route-detail'),
  path('edit/<int:route_id>/', edit_route, name='edit-route'),
  path('delete/<int:route_id>/', delete_route, name='delete-route') 
]