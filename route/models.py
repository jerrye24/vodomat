# coding=utf-8
from __future__ import unicode_literals
from django.db import models


class Route(models.Model):
    route_number = models.IntegerField(verbose_name='Номер маршрута')
    car_number = models.CharField(max_length=15, verbose_name='Номер автомобиля')
    driver1 = models.CharField(max_length=20, null=True, blank=True, verbose_name='Водитель 1')
    driver2 = models.CharField(max_length=20, null=True, blank=True, verbose_name='Водитель 2')

    def __unicode__(self):
        return '%s' % self.route_number

    class Meta:
        ordering = ('route_number', )
        db_table = 'route'
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты'
