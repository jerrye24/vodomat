from django.conf.urls import url
from .views import CollectionDayView, collection_period_form_view, collection_period_view


urlpatterns = [
    url(r'^(?P<year>\d{4})/(?P<month>\d+)/(?P<day>\d+)/$', CollectionDayView.as_view(), name='collection_day'),
    url(r'^period_form/$', collection_period_form_view, name='collection_period_form'),
    url(r'^(?P<start>\w+)/(?P<end>\w+)/(?P<id>\d+)/$', collection_period_view, name='collection_period'),
]