# coding=utf-8
from __future__ import unicode_literals
from django.db import models
from avtomat.models import Avtomat


class Collection(models.Model):
    time = models.DateTimeField(primary_key=True, verbose_name='Время')
    time_in_message = models.CharField(max_length=12, verbose_name='Время в сообщении')
    avtomat = models.ForeignKey(Avtomat, verbose_name='Автомат')
    how_money = models.FloatField(verbose_name='Сумма инкассации')

    def __unicode__(self):
        return '%s' % self.avtomat

    class Meta:
        ordering = ('-time', )
        db_table = 'collection'
        verbose_name = 'Икассация'
        verbose_name_plural = 'Инкассации'