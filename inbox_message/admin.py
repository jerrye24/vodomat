from django.contrib import admin
from .models import DataFromAvtomat


class DataFromAvtomatAdmin(admin.ModelAdmin):
    list_display = ('line', 'time', 'flag')
    list_filter = ('time', )
    search_fields = ('^line', )
    date_hierarchy = 'time'


admin.site.register(DataFromAvtomat, DataFromAvtomatAdmin)
