# coding=utf-8
from celery.task import periodic_task
from celery.schedules import crontab
from functions import parsing_line38, parsing_line48
from .models import DataFromAvtomat
from avtomat.models import Avtomat
from collection.models import Collection
from statistic.models import Statistic
from status.models import Status
import datetime
from dateutil.relativedelta import relativedelta


@periodic_task(name='data_to_table', ignor_result=True, run_every=crontab(minute='*/1'))
def data_to_table():
    lines = DataFromAvtomat.objects.filter(flag=False)
    for line in lines:
        string_from_avtomat = line.line
        time = line.time
        if len(string_from_avtomat) == 38:
            data = parsing_line38(string_from_avtomat)
            if data == 'error':
                continue
        elif len(string_from_avtomat) == 48:
            data = parsing_line48(string_from_avtomat)
            if data == 'error':
                continue
        try:
            avtomat = Avtomat.objects.get(number=data['number'])
        except Avtomat.DoesNotExist:
            avtomat = Avtomat(number=data['number'])
            avtomat.save()
        try:
            status = Status.objects.get(avtomat=avtomat)
        except Status.DoesNotExist:
            status = Status(avtomat=avtomat, time=time)
        if len(string_from_avtomat) == 48 and status.grn == data['grn']:
            status.ev_bill_time += int((time - status.time).total_seconds() / 60)
        else:
            status.ev_bill_time = 0
        if len(string_from_avtomat) == 48 and status.kop == data['kop']:
            status.ev_coin_time += int((time - status.time).total_seconds() / 60)
        else:
            status.ev_coin_time = 0
        status.time = time
        status.how_money = data['how_money']
        status.water_balance = data['water_balance']
        status.water_price = data['water_price']
        status.ev_water = data['ev_water']
        status.ev_bill = data['ev_bill']
        status.ev_volt = data['ev_volt']
        status.ev_counter_water = data['ev_counter_water']
        status.event = data['event']
        status.ev_register = data['ev_register']
        status.grn = data['grn']
        status.kop = data['kop']
        status.time_to_block = data['time_to_block']
        status.save()
        Statistic(avtomat=avtomat, time=time, water_balance=data['water_balance'], how_money=data['how_money'],
                  water_price=data['water_price'], ev_water=data['ev_water'], ev_bill=data['ev_bill'],
                  ev_volt=data['ev_volt'], ev_counter_water=data['ev_counter_water'], ev_register=data['ev_register'],
                  grn=data['grn'], kop=data['kop'], event=data['event']).save(force_insert=True)
        if data['event'] == 3:
            Collection(avtomat=avtomat, how_money=data['how_money'], time=time, time_in_message=data['time_in_message']).save(force_insert=True)
        line.delete()
        # line.flag = True
        # line.save()


@periodic_task(name='delete_old_statistic_collection', ignor_result=True, run_every=crontab(0, 2, day_of_month='1'))
def delete_old_statistic_collections():
    delete_month = datetime.date.today - relativedelta(months=-2)
    Statistic.objects.filter(time__lt=delete_month).delete()
    Collection.objects.filter(time__lt=delete_month).delete()


@periodic_task(name='delete_old_datafromavtomat', ignor_result=True, run_every=crontab(minute=0, hour=3))
def delete_old_datafromavtomat():
    delete_week = datetime.date.today() - relativedelta(weeks=-2)
    DataFromAvtomat.objects.filter(time__lt=delete_week).delete()
