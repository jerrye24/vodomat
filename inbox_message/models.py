# coding=utf-8
from __future__ import unicode_literals
from django.db import models


class DataFromAvtomat(models.Model):
    time = models.DateTimeField(primary_key=True, auto_now_add=True, verbose_name='Время')
    line = models.CharField(max_length=48, verbose_name='Строка от автомата')
    flag = models.BooleanField(default=False, verbose_name='Обработка строки')

    def __unicode__(self):
        return self.line

    class Meta:
        ordering = ('-time', )
        db_table = 'inbox_message'
        verbose_name = 'Строка от автомата'
        verbose_name_plural = 'Строки от автоматов'
