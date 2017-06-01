# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-01 09:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='route',
            name='driver',
        ),
        migrations.AddField(
            model_name='route',
            name='driver1',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='\u0412\u043e\u0434\u0438\u0442\u0435\u043b\u044c 1'),
        ),
        migrations.AddField(
            model_name='route',
            name='driver2',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='\u0412\u043e\u0434\u0438\u0442\u0435\u043b\u044c 2'),
        ),
    ]
