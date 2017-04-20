from django.contrib import admin
from vodomat.models import Status, Avtomat, Statistic, Collection, DataFromAvtomat, Route, City, Street


class DataFromAvtomatAdmin(admin.ModelAdmin):
    list_display = ('line', 'time', 'flag')
    list_filter = ('time', )
    search_fields = ('^line', )
    date_hierarchy = 'time'


class AvtomatAdmin(admin.ModelAdmin):
    list_display = ('number', 'street', 'house')
    list_filter = ('route__car_number', )
    search_fields = ('number',)


class RouteAdmin(admin.ModelAdmin):
    list_display = ('route_number', 'car_number', 'driver')


class StatusAdmin(admin.ModelAdmin):
    list_display = ('avtomat', 'time')
    list_filter = ('time', )
    search_fields = ('avtomat__number', )
    date_hierarchy = 'time'


class StatisticAdmin(admin.ModelAdmin):
    list_display = ('avtomat', 'time', 'water_balance', 'how_money')
    list_filter = ('time',)
    search_fields = ('avtomat__number', )
    date_hierarchy = 'time'


class CollectionAdmin(admin.ModelAdmin):
    list_display = ('avtomat', 'how_money', 'time')
    list_filter = ('time', )
    search_fields = ('avtomat__number', )
    date_hierarchy = 'time'

admin.site.register(Status, StatusAdmin)
admin.site.register(Statistic, StatisticAdmin)
admin.site.register(Avtomat, AvtomatAdmin)
admin.site.register(City)
admin.site.register(Street)
admin.site.register(Route, RouteAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(DataFromAvtomat, DataFromAvtomatAdmin)