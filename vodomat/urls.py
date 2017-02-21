from django.conf.urls import url
from vodomat.views import *

app_name = 'vodomat'
urlpatterns = [
    url(r'^$', status_view, name='status'),
    url(r'^avtomat/$', AvtomatView.as_view(), name='avtomat'),
    url(r'^detail_avtomat/(?P<id>\d+)/$', detail_avtomat_view, name='detail_avtomat'),
    url(r'^edit_avtomat/(?P<pk>\d+)/$', EditAvtomatView.as_view(), name='edit_avtomat'),
    url(r'^collection/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/$', CollectionDayView.as_view(), name='collection'),
    url(r'^collection_period_form/$', collection_period_form_view, name='collection_period_form'),
    url(r'^collection_period/(?P<start>\w+)/(?P<end>\w+)/(?P<id>\d+)/$', collection_period_view, name='collection_period'),
    url(r'^collection_route/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/$', collection_route_view, name='collection_route'),
    url(r'^collection_missing/$', collection_missing_view, name='collection_missing'),
    url(r'^statistic_form/$', statistic_form_view, name='statistic_form'),
    url(r'^statistic/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/(?P<id>\d+)/$', StatisticDayView.as_view(), name='statistic'),
    url(r'^statistic_period_form/$', statistic_period_form_view, name='statistic_period_form'),
    url(r'^statistic_period/(?P<start>\d+)/(?P<end>\d+)/(?P<id>\d+)', statistic_period_view, name='statistic_period'),
    url(r'^route/$', RouteView.as_view(), name='route'),
    url(r'^route/(?P<route>.{0,15})/$', RouteSortedView.as_view(), name='route_sorted'),
    url(r'^route_create/$', CreateRouteView.as_view(), name='create_route'),
    url(r'^route_edit/(?P<pk>\d+)/$', EditRouteView.as_view(), name='edit_route'),
    url(r'^route_delete/(?P<pk>\d+)/$', delete_route_view, name='delete_route'),
    url(r'^visualization/(?P<year>\d+)/(?P<month>\d+)/(?P<id>\d+)/$', visualization_view, name='visualization'),
    url(r'^map/$', map_view, name='map'),
    url(r'^(\w)/$', SearchView.as_view(), name='search'),
    url(r'^detail/(?P<number>\d+)/$', detail_mobile_view, name='detail_mobile'),
]
