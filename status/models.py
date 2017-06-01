# coding=utf-8
from __future__ import unicode_literals
from django.db import models
from avtomat.models import Avtomat


class Status(models.Model):
    avtomat = models.ForeignKey(Avtomat, verbose_name='Автомат')
    time = models.DateTimeField(verbose_name='Время')
    water_balance = models.FloatField(verbose_name='Остаток воды в автомате')
    how_money = models.FloatField(verbose_name='Принятая сумма')
    grn = models.IntegerField(default=0, verbose_name='Грн')
    kop = models.IntegerField(default=0, verbose_name='Коп')
    water_price = models.FloatField(verbose_name='Цена за один литр')
    ev_water = models.BooleanField(verbose_name='Наличие воды')
    ev_bill = models.BooleanField(verbose_name='Купюроприемник')
    ev_bill_time = models.IntegerField(default=0, verbose_name='Купюроприемник время')
    ev_coin_time = models.IntegerField(default=0, verbose_name='Монетоприемник время')
    ev_volt = models.BooleanField(verbose_name='Электросеть')
    ev_counter_water = models.BooleanField(verbose_name='Счетчик воды')
    ev_register = models.BooleanField(default=0, verbose_name='Регистратор')
    time_to_block = models.IntegerField(default=99, verbose_name='Время до блокировки')

    def __unicode__(self):
        return '%s' % self.avtomat

    class Meta:
        ordering = ('-time', )
        db_table = 'status'
        verbose_name = 'Статус'
        verbose_name_plural = 'Статуc'
