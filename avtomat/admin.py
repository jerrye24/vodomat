from django.contrib import admin
from .models import Avtomat, City, Street


class AvtomatAdmin(admin.ModelAdmin):
    list_display = ('number', 'street', 'house')
    list_filter = ('route__car_number', )
    search_fields = ('number',)


admin.site.register(Avtomat, AvtomatAdmin)
admin.site.register(City)
admin.site.register(Street)
