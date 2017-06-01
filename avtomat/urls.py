from django.conf.urls import url
from .views import AvtomatView, avtomat_form_view, street_json_view, StreetView, StreetCreateView, StreetEditView, CityView, CityCreateView, CityEditView

urlpatterns = [
    url(r'^$', AvtomatView.as_view(), name='avtomat'),
    url(r'^(?P<pk>\d+)/$', avtomat_form_view, name='avtomat_form'),
    url(r'^street_json/$', street_json_view, name='street_json'),
    url(r'^street/$', StreetView.as_view(), name='street'),
    url(r'^street_create/$', StreetCreateView.as_view(), name='street_create'),
    url(r'^street_edit/(?P<pk>\d+)/$', StreetEditView.as_view(), name='street_edit'),
    url(r'^city/$', CityView.as_view(), name='city'),
    url(r'^city_create/$', CityCreateView.as_view(), name='city_create'),
    url(r'^city_edit/(?P<pk>\d+)/$', CityEditView.as_view(), name='city_edit')
]
