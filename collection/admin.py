from django.contrib import admin
from .models import Collection


class CollectionAdmin(admin.ModelAdmin):
    list_display = ('avtomat', 'how_money', 'time')
    list_filter = ('time', )
    search_fields = ('avtomat__number', )
    date_hierarchy = 'time'


admin.site.register(Collection, CollectionAdmin)