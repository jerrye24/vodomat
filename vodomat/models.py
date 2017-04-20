#coding: utf8
from __future__ import unicode_literals
from django.db import models
from yandex_maps import api


class DataFromAvtomat(models.Model):
    time = models.DateTimeField(auto_now_add=True, verbose_name='Время')
    line = models.CharField(max_length=48, verbose_name='Строка от автомата')
    flag = models.BooleanField(default=False, verbose_name='Обработка строки')

    def __unicode__(self):
        return self.line

    class Meta:
        ordering = ('-time', )
        db_table = 'inbox_http'
        verbose_name = 'Строка от автомата'
        verbose_name_plural = 'Строки от автоматов'


class Route(models.Model):
    route_number = models.IntegerField(verbose_name='Номер маршрута')
    car_number = models.CharField(max_length=15, verbose_name='Номер автомобиля')
    driver = models.CharField(max_length=50, verbose_name='Водитель')

    def __unicode__(self):
        return '%s' % self.route_number

    class Meta:
        ordering = ('route_number', )
        db_table = 'route'
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты'


class City(models.Model):
    city = models.CharField(max_length=20, verbose_name='Город')

    def __unicode__(self):
        return self.city

    class Meta:
        db_table = 'city'
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class Street(models.Model):
    city = models.ForeignKey(City, verbose_name='Город')
    street = models.CharField(max_length=50, verbose_name='Улица')

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
            return '%s %s' % (self.street, self.house)
        else:
            return 'Новый автомат %s' % self.number

    def save(self, *args, **kwargs):
        if not self.latitude or not self.longitude:
            if self.street and self.house:
                api_key = 'ADaLpFgBAAAACEUSYwIA_B3Gfz1rX3FtQFNBCpOTNECtaLMAAAAAAAAAAACqjWNy3U75ctVOCDY2TocWqQLlQQ=='
                address = u'%s, %s, %s' % (self.street.city, self.street, self.house)
                pos = api.geocode(api_key, address)
                self.latitude = float(pos[1])
                self.longitude = float(pos[0])
        super(Avtomat, self).save(*args, **kwargs)

    class Meta:
        ordering = ['street', '-house']
        db_table = 'avtomat'
        verbose_name = 'Автомат'
        verbose_name_plural = 'Автоматы'


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


class Statistic(models.Model):
    time = models.DateTimeField(verbose_name='Время')
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
        db_table = 'avtomat_log_table'
        verbose_name = 'Статистика'
        verbose_name_plural = 'Статистика'


class Collection(models.Model):
    time = models.DateTimeField(verbose_name='Время')
    time_in_message = models.CharField(max_length=12, verbose_name='Время в сообщении')
    avtomat = models.ForeignKey(Avtomat, verbose_name='Автомат')
    how_money = models.FloatField(verbose_name='Сумма инкассации')

    def __unicode__(self):
        return '%s' % self.avtomat

    class Meta:
        ordering = ('-time', )
        db_table = 'avtomat_coll_table'
        verbose_name = 'Икассация'
        verbose_name_plural = 'Инкассации'
