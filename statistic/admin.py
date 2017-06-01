from django.contrib import admin
from .models import Statistic


class StatisticAdmin(admin.ModelAdmin):
    list_display = ('avtomat', 'time', 'water_balance', 'how_money')
    list_filter = ('time',)
    search_fields = ('avtomat__number', )
    date_hierarchy = 'time'


admin.site.register(Statistic, StatisticAdmin)
