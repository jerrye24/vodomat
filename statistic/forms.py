# coding=utf-8
from avtomat.models import Avtomat
from django import forms


class UIWidget(forms.TextInput):
    class Media:
        css = {'all': ('//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css', )}
        js = ('https://code.jquery.com/ui/1.12.1/jquery-ui.js', )


class StatisticForm(forms.Form):
    avtomat = forms.ModelChoiceField(queryset=Avtomat.objects.all(), label=u'Адрес')
    period = forms.CharField(widget=UIWidget, label=u'Период')

    def clean_period(self):
        data = self.cleaned_data['period']
        period = data.split('-')
        for data in period:
            if int(data[:2]) > 31 or int(data[2:4]) > 12 or int(data[:2]) < 1 or int(data[2:4]) < 1:
                raise forms.ValidationError('Неверный период!!!')
        return period
