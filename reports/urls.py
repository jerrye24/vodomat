from django.conf.urls import url
from .views import reports

urlpatterns = [
    url(r'^$', reports, name='reports'),
]