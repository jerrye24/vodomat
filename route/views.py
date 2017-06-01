from django.shortcuts import redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView
from .models import Route


class RouteView(LoginRequiredMixin, ListView):
    model = Route
    template_name = 'route/route.html'
    context_object_name = 'route_table'


class RouteCreateView(LoginRequiredMixin, CreateView):
    model = Route
    fields = ['route_number', 'car_number', 'driver1', 'driver2']
    template_name = 'route/route_create.html'

    def get_success_url(self):
        return reverse('route')


class RouteEditView(LoginRequiredMixin, UpdateView):
    model = Route
    fields = ['route_number', 'car_number', 'driver1', 'driver2']
    template_name = 'route/route_edit.html'

    def get_success_url(self):
        return reverse('route')


@login_required
def route_delete_view(request, pk):
    Route.objects.get(id=pk).delete()
    return redirect('route')