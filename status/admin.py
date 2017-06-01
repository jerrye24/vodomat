from django.contrib import admin
from .models import Status


class StatusAdmin(admin.ModelAdmin):
    list_display = ('avtomat', 'time')
    list_filter = ('time',)
    search_fields = ('avtomat__number',)
    date_hierarchy = 'time'


admin.site.register(Status, StatusAdmin)
