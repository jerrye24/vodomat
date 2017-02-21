from django.contrib import admin
from vodomat.models import Status, Avtomat, Statistic, Collection, DataFromAvtomat, Route

class DataFromAvtomatAdmin(admin.ModelAdmin):
    list_display = ('line', 'time', 'flag')
    list_filter = ('time', )
    search_fields = ('^line', )
    date_hierarchy = 'time'

class AvtomatAdmin(admin.ModelAdmin):
    list_display = ('address', 'city', 'number')
    search_fields = ('address', 'number')
    list_filter = ('route__car_number', )

class RouteAdmin(admin.ModelAdmin):
    list_display = ('car_number', 'driver')

class StatusAdmin(admin.ModelAdmin):
    list_display = ('avtomat', 'time')
    list_filter = ('avtomat__route__car_number', )
    search_fields = ('avtomat__address', )

class StatisticAdmin(admin.ModelAdmin):
    list_display = ('avtomat', 'time', 'water_balance', 'how_money')
    list_filter = ('time',)
    search_fields = ('avtomat__address', )
    date_hierarchy = 'time'

class CollectionAdmin(admin.ModelAdmin):
    list_display = ('avtomat', 'how_money', 'time')
    list_filter = ('time', )
    search_fields = ('avtomat__address', )
    date_hierarchy = 'time'

admin.site.register(Status, StatusAdmin)
admin.site.register(Statistic, StatisticAdmin)
admin.site.register(Avtomat, AvtomatAdmin)
admin.site.register(Route, RouteAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(DataFromAvtomat, DataFromAvtomatAdmin)