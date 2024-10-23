from django.shortcuts import render, get_object_or_404, redirect
from .models import Route
from .forms import RouteForm, VehicleAssignForm

def routes_list(request):
  routes = Route.objects.all()
  return render(request, 'routes-list.html', {'routes': routes})


def route_details(request, route_id):
  route = get_object_or_404(Route, id=route_id)
  return render(request, 'route-details.html', {'route': route})


def add_route(request):
  if request.method == 'POST':
    form = RouteForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('routes-list')
  else:
    form = RouteForm()
  return render(request, 'add-route.html', {'form': form})


def edit_route(request, route_id):
  route = get_object_or_404(Route, id=route_id)
  if request.method == 'POST':
    form = RouteForm(request.POST, instance=route)
    if form.is_valid():
      form.save()
      return redirect('route-details', route_id=route.id)
  else:
    form = RouteForm(instance=route)
  return render(request, 'edit-route.html', {'form': form, 'route': route})


def delete_route(request, route_id):
  route = get_object_or_404(Route, id=route_id)
  if request.method == 'POST':
    route.delete()
    return redirect('routes-list')
  return render(request, 'delete-route.html', {'route': route})


def assign_vehicles(request, route_id):
  route = get_object_or_404(Route, id=route_id)
  
  if request.method == 'POST':
    form = VehicleAssignForm(request.POST)
    if form.is_valid():
      vehicles = form.cleaned_data['vehicles']
      for vehicle in vehicles:
        vehicle.route = route 
        vehicle.save()
      return redirect('route-details', route_id=route_id) 
  else:
    form = VehicleAssignForm()
  
  return render(request, 'assign-vehicles.html', {'route': route, 'form': form})