# coding=utf-8

"""vodomat_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout_then_login
from inbox_message.views import data_from_avtomat

# urlpatterns = [
#     url(r'^login/$', login, name='login'),
#     url(r'^logout/$', logout_then_login, name='logout'),
#     url(r'^admin/', admin.site.urls),
#     url(r'^ufkc721.php', data_from_avtomat, name='data_from_avtomat'),
#     url(r'^$', status_view, name='status'),
#     url(r'^avtomat/$', AvtomatView.as_view(), name='avtomat'),
#     url(r'^avtomat_detail/(?P<id>\d+)/$', detail_avtomat_view, name='detail_avtomat'),
#     url(r'^avtomat_edit/(?P<pk>\d+)/$', edit_avtomat_form_view, name='edit_avtomat'),
#     url(r'^street_json/$', street_json_view, name='street_json'),
# #    url(r'^edit_avtomat/(?P<pk>\d+)/$', EditAvtomatView.as_view(), name='edit_avtomat'),
#     url(r'^collection/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/$', CollectionDayView.as_view(), name='collection'),
#     url(r'^collection_period_form/$', collection_period_form_view, name='collection_period_form'),
#     url(r'^collection_period/(?P<start>\w+)/(?P<end>\w+)/(?P<id>\d+)/$', collection_period_view, name='collection_period'),
#     url(r'^collection_route/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/$', collection_route_view, name='collection_route'),
#     url(r'^collection_missing/$', collection_missing_view, name='collection_missing'),
#     url(r'^statistic_form/$', statistic_form_view, name='statistic_form'),
#     url(r'^statistic/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/(?P<id>\d+)/$', StatisticDayView.as_view(), name='statistic'),
#     url(r'^statistic_period_form/$', statistic_period_form_view, name='statistic_period_form'),
#     url(r'^statistic_period/(?P<start>\d+)/(?P<end>\d+)/(?P<id>\d+)', statistic_period_view, name='statistic_period'),
#     url(r'^route/$', RouteView.as_view(), name='route'),
#     url(r'^route_list/$', RouteListView.as_view(), name='route_list'),
#     url(r'^route_create/$', CreateRouteView.as_view(), name='create_route'),
#     url(r'^route_edit/(?P<pk>\d+)/$', EditRouteView.as_view(), name='edit_route'),
#     url(r'^route_delete/(?P<pk>\d+)/$', delete_route_view, name='delete_route'),
#     url(r'^route/(?P<route>.{0,15})/$', RouteSortedView.as_view(), name='route_sorted'),
#     url(r'^city/$', CityView.as_view(), name='city'),
#     url(r'^city_create/$', CreateCityView.as_view(), name='create_city'),
#     url(r'^city_edit/(?P<pk>\d+)/$', EditCityView.as_view(), name='edit_city'),
#     url(r'^street/$', StreetView.as_view(), name='street'),
#     url(r'^street_create/$', CreateStreetView.as_view(), name='create_street'),
#     url(r'^street_edit/(?P<pk>\d+)/$', EditStreetView.as_view(), name='edit_street'),
#     url(r'^visualization/(?P<year>\d+)/(?P<month>\d+)/(?P<id>\d+)/$', visualization_view, name='visualization'),
#     url(r'^map/$', map_view, name='map'),
#     url(r'^(\w)/$', SearchView.as_view(), name='search'),
#     url(r'^detail/(?P<number>\d+)/$', detail_mobile_view, name='detail_mobile'),
# ]


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', login, name='login'),
    url(r'^logout', logout_then_login, name='logout'),

    url(r'^ufkc721.php', data_from_avtomat, name='data_from_avtomat'),
    url(r'^avtomat/', include('avtomat.urls')),
    url(r'^route/', include('route.urls')),
    url(r'^status/', include('status.urls')),
    url(r'^collection/', include('collection.urls')),
    url(r'^statistic/', include('statistic.urls')),

]


admin.site.site_header = 'Администрирование Vodomat'
admin.site.site_title = 'Администрирование Vodomat'
admin.site.site_url = '/status/'

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]

