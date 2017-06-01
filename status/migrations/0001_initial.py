# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-01 11:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('avtomat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(verbose_name='\u0412\u0440\u0435\u043c\u044f')),
                ('water_balance', models.FloatField(verbose_name='\u041e\u0441\u0442\u0430\u0442\u043e\u043a \u0432\u043e\u0434\u044b \u0432 \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0435')),
                ('how_money', models.FloatField(verbose_name='\u041f\u0440\u0438\u043d\u044f\u0442\u0430\u044f \u0441\u0443\u043c\u043c\u0430')),
                ('grn', models.IntegerField(default=0, verbose_name='\u0413\u0440\u043d')),
                ('kop', models.IntegerField(default=0, verbose_name='\u041a\u043e\u043f')),
                ('water_price', models.FloatField(verbose_name='\u0426\u0435\u043d\u0430 \u0437\u0430 \u043e\u0434\u0438\u043d \u043b\u0438\u0442\u0440')),
                ('ev_water', models.BooleanField(verbose_name='\u041d\u0430\u043b\u0438\u0447\u0438\u0435 \u0432\u043e\u0434\u044b')),
                ('ev_bill', models.BooleanField(verbose_name='\u041a\u0443\u043f\u044e\u0440\u043e\u043f\u0440\u0438\u0435\u043c\u043d\u0438\u043a')),
                ('ev_bill_time', models.IntegerField(default=0, verbose_name='\u041a\u0443\u043f\u044e\u0440\u043e\u043f\u0440\u0438\u0435\u043c\u043d\u0438\u043a \u0432\u0440\u0435\u043c\u044f')),
                ('ev_coin_time', models.IntegerField(default=0, verbose_name='\u041c\u043e\u043d\u0435\u0442\u043e\u043f\u0440\u0438\u0435\u043c\u043d\u0438\u043a \u0432\u0440\u0435\u043c\u044f')),
                ('ev_volt', models.BooleanField(verbose_name='\u042d\u043b\u0435\u043a\u0442\u0440\u043e\u0441\u0435\u0442\u044c')),
                ('ev_counter_water', models.BooleanField(verbose_name='\u0421\u0447\u0435\u0442\u0447\u0438\u043a \u0432\u043e\u0434\u044b')),
                ('ev_register', models.BooleanField(default=0, verbose_name='\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440')),
                ('time_to_block', models.IntegerField(default=99, verbose_name='\u0412\u0440\u0435\u043c\u044f \u0434\u043e \u0431\u043b\u043e\u043a\u0438\u0440\u043e\u0432\u043a\u0438')),
                ('avtomat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='avtomat.Avtomat', verbose_name='\u0410\u0432\u0442\u043e\u043c\u0430\u0442')),
            ],
            options={
                'ordering': ('-time',),
                'db_table': 'status',
                'verbose_name': '\u0421\u0442\u0430\u0442\u0443\u0441',
                'verbose_name_plural': '\u0421\u0442\u0430\u0442\u0443c',
            },
        ),
    ]
