# coding=utf-8
from __future__ import unicode_literals
from django.db import models
import googlemaps
from route.models import Route


class City(models.Model):
    city = models.CharField(max_length=20, unique=True, verbose_name='Город')

    def __unicode__(self):
        return self.city

    class Meta:
        db_table = 'city'
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class Street(models.Model):
    city = models.ForeignKey(City, verbose_name='Город')
    street = models.CharField(max_length=50, unique=True, verbose_name='Улица')

    def __unicode__(self):
        return self.street

    class Meta:
        db_table = 'street'
        verbose_name = 'Улица'
        verbose_name_plural = 'Улицы'


class Avtomat(models.Model):

    SIZE_OF_AVTOMAT = (
        (470, u'Одинарный'),
        (940, u'Двойной'),
    )

    number = models.IntegerField(verbose_name='Номер автомата')
    street = models.ForeignKey(Street, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Улица')
    house = models.CharField(max_length=10, blank=True, null=True, verbose_name='Номер дома')
    latitude = models.FloatField(blank=True, null=True, verbose_name='Широта')
    longitude = models.FloatField(blank=True, null=True, verbose_name='Долгота')
    route = models.ForeignKey(Route, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Маршрут')
    water_price = models.IntegerField(blank=True, null=True, verbose_name='Цена за один литр')
    size = models.IntegerField(blank=True, null=True, choices=SIZE_OF_AVTOMAT, verbose_name='Обьем автомата')
    phone = models.CharField(max_length=12, blank=True, null=True, verbose_name='Телефон')
    register = models.IntegerField(blank=True, null=True, verbose_name='Номер регистратора')
    security = models.IntegerField(blank=True, null=True, verbose_name='Охранный обьект')
    competitors = models.BooleanField(default=False, verbose_name='Конкуренты')

    def __unicode__(self):
        if self.street:
            if self.street.city.city == 'Харьков':
                return '%s %s' % (self.street, self.house)
            else:
                return '%s %s(%s)' % (self.street, self.house, self.street.city)
        else:
            return 'Новый автомат %s' % self.number

    def save(self, *args, **kwargs):
        if self.street and self.house:
            try:
                api_key = 'AIzaSyB3wwrPtsRIyV2twvjKvHAwE-Q3aNx5Yjs'
                address = u'%s, %s, %s' % (self.street.city, self.street, self.house)
                gmap = googlemaps.Client(key=api_key)
                geocode_result = gmap.geocode(address)
                position = geocode_result[0]['geometry']['location']
                self.latitude = position['lat']
                self.longitude = position['lng']
            except IndexError:
                pass
        super(Avtomat, self).save(*args, **kwargs)

    class Meta:
        ordering = ['street', '-house']
        db_table = 'avtomat'
        verbose_name = 'Автомат'
        verbose_name_plural = 'Автоматы'