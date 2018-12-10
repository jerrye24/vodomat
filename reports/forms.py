# coding=utf-8
from django import forms


class BilliardsActivityForm(forms.Form):
    start_period = forms.TimeField(label=u'Начало периода')
    end_period = forms.TimeField(label=u'Конец периода')
    sum = forms.IntegerField(label=u'Сумма')