from django.conf.urls import url
from .views import RouteView, RouteCreateView, RouteEditView, route_delete_view


urlpatterns = [
    url(r'^$', RouteView.as_view(), name='route'),
    url(r'^create/$', RouteCreateView.as_view(), name='route_create'),
    url(r'^edit/(?P<pk>\d+)/$', RouteEditView.as_view(), name='route_edit'),
    url(r'^delete/(?P<pk>\d+)', route_delete_view, name='route_delete'),
]