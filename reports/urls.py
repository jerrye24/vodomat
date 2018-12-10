from django.conf.urls import url
from .views import reports, billiards_activity_form, billiards_activity, coins_activity_form, coins_activity


urlpatterns = [
    url(r'^$', reports, name='reports'),
    url(r'^billiards_activity_form/$', billiards_activity_form, name='billiards_activity_form'),
    url(r'^billiards_activity/$', billiards_activity, name='billiards_activity'),
    url(r'^coins_activity_form/$', coins_activity_form, name='coins_activity_form'),
    url(r'^coins_activity/$', coins_activity, name='coins_activity'),
]