from django.shortcuts import render, get_object_or_404, redirect
from .models import Route
from .forms import RouteForm
from vehicles.models import Vehicle
from django.contrib.auth.decorators import login_required

@login_required
def routes_list(request):
  routes = Route.objects.all()
  return render(request, 'routes-list.html', {'routes': routes})


@login_required
def route_details(request, route_id):
  route = get_object_or_404(Route, id=route_id)
  return render(request, 'route-details.html', {'route': route})


@login_required
def add_route(request):
  if request.method == 'POST':
    form = RouteForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('routes-list')
  else:
    form = RouteForm()
  return render(request, 'add-route.html', {'form': form})


@login_required
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


@login_required
def delete_route(request, route_id):
  route = get_object_or_404(Route, id=route_id)
  if request.method == 'POST':
    route.delete()
    return redirect('routes-list')
  return render(request, 'delete-route.html', {'route': route})


@login_required
def assign_vehicles_to_route(request, route_id):
  route = get_object_or_404(Route, id=route_id)
  
  if request.method == 'POST':
    vehicle_ids = request.POST.getlist('vehicles')
    selected_vehicles = Vehicle.objects.filter(id__in=vehicle_ids)
    route.vehicles.exclude(id__in=vehicle_ids).update(route=None)
    selected_vehicles.update(route=route)
    
    return redirect('routes-list')
  
  else:
    available_vehicles = Vehicle.objects.filter(route__isnull=True)
    assigned_vehicles = route.vehicles.all()
    all_vehicles = available_vehicles | assigned_vehicles
    
    return render(request, 'assign-vehicles.html', {
      'route': route,
      'vehicles': all_vehicles,
      'assigned_vehicles': assigned_vehicles
    })