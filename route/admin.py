from django.contrib import admin
from .models import Route


class RouteAdmin(admin.ModelAdmin):
    list_display = ('route_number', 'car_number', 'driver1', 'driver2')


admin.site.register(Route, RouteAdmin)
