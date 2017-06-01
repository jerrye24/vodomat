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

