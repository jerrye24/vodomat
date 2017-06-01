# coding=utf-8
from __future__ import unicode_literals
from django.db import models
from avtomat.models import Avtomat


class Statistic(models.Model):
    time = models.DateTimeField(primary_key=True, verbose_name='Время')
    avtomat = models.ForeignKey(Avtomat, verbose_name='Автомат')
    water_balance = models.FloatField(verbose_name='Остаток воды в автомате')
    how_money = models.FloatField(verbose_name='Принятая сумма')
    water_price = models.FloatField(verbose_name='Цена за литр воды')
    ev_water = models.BooleanField(verbose_name='Наличие воды')
    ev_bill = models.BooleanField(verbose_name='Купюроприемник')
    ev_volt = models.BooleanField(verbose_name='Электросеть')
    ev_counter_water = models.BooleanField(verbose_name='Счетчик воды')
    ev_register = models.BooleanField(default=0, verbose_name='Регистратор')
    grn = models.IntegerField(default=0, verbose_name='Гривны')
    kop = models.IntegerField(default=0, verbose_name='Копейки')
    event = models.IntegerField(verbose_name='Событие')

    def __unicode__(self):
        return '%s' % self.avtomat

    class Meta:
        ordering = ('-time', )
        db_table = 'statistic'
        verbose_name = 'Статистика'
        verbose_name_plural = 'Статистика'