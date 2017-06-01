from django.conf.urls import url
from .views import statistic_form_view, statistic_view


urlpatterns = [
    url(r'^statistic_form/$', statistic_form_view, name='statistic_form'),
    url(r'^(?P<start>\d+)/(?P<end>\d+)/(?P<id>\d+)/$', statistic_view, name='statistic'),
]