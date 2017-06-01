# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-29 13:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('route', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avtomat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='\u041d\u043e\u043c\u0435\u0440 \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0430')),
                ('house', models.CharField(blank=True, max_length=10, null=True, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u0434\u043e\u043c\u0430')),
                ('latitude', models.FloatField(blank=True, null=True, verbose_name='\u0428\u0438\u0440\u043e\u0442\u0430')),
                ('longitude', models.FloatField(blank=True, null=True, verbose_name='\u0414\u043e\u043b\u0433\u043e\u0442\u0430')),
                ('water_price', models.IntegerField(blank=True, null=True, verbose_name='\u0426\u0435\u043d\u0430 \u0437\u0430 \u043e\u0434\u0438\u043d \u043b\u0438\u0442\u0440')),
                ('size', models.IntegerField(blank=True, choices=[(470, '\u041e\u0434\u0438\u043d\u0430\u0440\u043d\u044b\u0439'), (940, '\u0414\u0432\u043e\u0439\u043d\u043e\u0439')], null=True, verbose_name='\u041e\u0431\u044c\u0435\u043c \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0430')),
                ('phone', models.CharField(blank=True, max_length=12, null=True, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d')),
                ('register', models.IntegerField(blank=True, null=True, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440\u0430')),
                ('security', models.IntegerField(blank=True, null=True, verbose_name='\u041e\u0445\u0440\u0430\u043d\u043d\u044b\u0439 \u043e\u0431\u044c\u0435\u043a\u0442')),
                ('competitors', models.BooleanField(default=False, verbose_name='\u041a\u043e\u043d\u043a\u0443\u0440\u0435\u043d\u0442\u044b')),
                ('route', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='route.Route', verbose_name='\u041c\u0430\u0440\u0448\u0440\u0443\u0442')),
            ],
            options={
                'ordering': ['street', '-house'],
                'db_table': 'avtomat',
                'verbose_name': '\u0410\u0432\u0442\u043e\u043c\u0430\u0442',
                'verbose_name_plural': '\u0410\u0432\u0442\u043e\u043c\u0430\u0442\u044b',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=20, verbose_name='\u0413\u043e\u0440\u043e\u0434')),
            ],
            options={
                'db_table': 'city',
                'verbose_name': '\u0413\u043e\u0440\u043e\u0434',
                'verbose_name_plural': '\u0413\u043e\u0440\u043e\u0434\u0430',
            },
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=50, verbose_name='\u0423\u043b\u0438\u0446\u0430')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='avtomat.City', verbose_name='\u0413\u043e\u0440\u043e\u0434')),
            ],
            options={
                'db_table': 'street',
                'verbose_name': '\u0423\u043b\u0438\u0446\u0430',
                'verbose_name_plural': '\u0423\u043b\u0438\u0446\u044b',
            },
        ),
        migrations.AddField(
            model_name='avtomat',
            name='street',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='avtomat.Street', verbose_name='\u0423\u043b\u0438\u0446\u0430'),
        ),
    ]
