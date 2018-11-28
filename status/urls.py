from django.conf.urls import url
from .views import StatusView, StatusAlphabetView, status_detail_view, status_map_view, status_search_form


urlpatterns = [
    url(r'^$', StatusView.as_view(), name='status'),
    url(r'^(\w)/$', StatusAlphabetView.as_view(), name='status_alphabet'),
    url(r'^status_detail/(?P<id>\d+)/$', status_detail_view, name='status_detail'),
    url(r'^search_status_form/$', status_search_form, name='status_search_form'),
    url(r'^map/$', status_map_view, name='status_map'),
]