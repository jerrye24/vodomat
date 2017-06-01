from django.conf.urls import url
from .views import StatusView, StatusAlphabetView, status_detail_view, status_map_view


urlpatterns = [
    url(r'^$', StatusView.as_view(), name='status'),
    url(r'^(\w)/$', StatusAlphabetView.as_view(), name='status_alphabet'),
    url(r'^(?P<id>\d+)', status_detail_view, name='status_detail'),
    url(r'^map/$', status_map_view, name='status_map'),
]