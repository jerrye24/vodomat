#coding: utf8
from __future__ import unicode_literals
from django.db import models
from yandex_maps import api


class DataFromAvtomat(models.Model):
    time = models.DateTimeField(primary_key=True, auto_now_add=True, verbose_name='Время')
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


class Avtomat(models.Model):
    CITY = (
        ('Харьков', 'Харьков'),
        ('Бабаи', 'Бабаи'),
        ('Безлюдовка', 'Безлюдовка'),
        ('Дергачи', 'Дергачи'),
        ('Малая Даниловка', 'Малая Даниловка'),
        ('Песочин', 'Песочин'),
        ('Покотиловка', 'Покотиловка'),
    )
    number = models.IntegerField(verbose_name='Номер автомата')
    city = models.CharField(max_length=20, verbose_name='Город', choices=CITY, default='Харьков')
    address = models.CharField(max_length=50, verbose_name='Адрес автомата')
    latitude = models.FloatField(default=0, verbose_name='Широта')
    longitude = models.FloatField(default=0, verbose_name='Долгота')
    route = models.ForeignKey(Route, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Маршрут')
    water_price = models.IntegerField(blank=True, null=True, verbose_name='Цена за один литр')
    size = models.IntegerField(blank=True, null=True, verbose_name='Обьем автомата')
    phone = models.IntegerField(blank=True, null=True, verbose_name='Телефон')
    register = models.IntegerField(blank=True, null=True, verbose_name='Номер регистратора')
    security = models.IntegerField(blank=True, null=True, verbose_name='Охранный обьект')
    interval = models.IntegerField(default=5, verbose_name='Интервал отправки данных')
    competitors = models.BooleanField(default=False, verbose_name='Конкуренты')

    def __unicode__(self):
        return self.address

    def save(self, *args, **kwargs):
        if self.address.find(u'Новый автомат') == -1:
            api_key = 'ADaLpFgBAAAACEUSYwIA_B3Gfz1rX3FtQFNBCpOTNECtaLMAAAAAAAAAAACqjWNy3U75ctVOCDY2TocWqQLlQQ=='
            address = u'%s, %s' % (self.city, self.address)
            pos = api.geocode(api_key, address)
            try:
        	self.latitude = float(pos[1])
        	self.longitude = float(pos[0])
	    except:
		pass
        super(Avtomat, self).save(*args, **kwargs)

    class Meta:
        ordering = ('address', )
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
        db_table = 'avtomat_log_table'
        verbose_name = 'Статистика'
        verbose_name_plural = 'Статистика'


class Collection(models.Model):
    time = models.DateTimeField(primary_key=True, verbose_name='Время')
    avtomat = models.ForeignKey(Avtomat, verbose_name='Автомат')
    how_money = models.FloatField(verbose_name='Сумма инкассации')

    def __unicode__(self):
        return '%s' % self.avtomat

    class Meta:
        ordering = ('-time', )
        db_table = 'avtomat_coll_table'
        verbose_name = 'Икассация'
        verbose_name_plural = 'Инкассации'
