# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-01 11:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataFromAvtomat',
            fields=[
                ('time', models.DateTimeField(auto_now_add=True, primary_key=True, serialize=False, verbose_name='\u0412\u0440\u0435\u043c\u044f')),
                ('line', models.CharField(max_length=48, verbose_name='\u0421\u0442\u0440\u043e\u043a\u0430 \u043e\u0442 \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0430')),
                ('flag', models.BooleanField(default=False, verbose_name='\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0430 \u0441\u0442\u0440\u043e\u043a\u0438')),
            ],
            options={
                'ordering': ('-time',),
                'db_table': 'inbox_message',
                'verbose_name': '\u0421\u0442\u0440\u043e\u043a\u0430 \u043e\u0442 \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0430',
                'verbose_name_plural': '\u0421\u0442\u0440\u043e\u043a\u0438 \u043e\u0442 \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u043e\u0432',
            },
        ),
    ]