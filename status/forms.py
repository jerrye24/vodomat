# coding=utf-8
from avtomat.models import Avtomat
from django import forms


class UIWidget(forms.Form):
    class Media:
        css = {'all': ('//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css', )}
        js = ('https://code.jquery.com/ui/1.12.1/jquery-ui.js', )


class StatusSearchForm(UIWidget):
    avtomat_label = forms.CharField(widget=forms.TextInput(attrs={'autofocus': 1, 'class': 'form-control', 'placeholder': u'Ввелите адрес автомата'}), label='')
    id = forms.IntegerField(widget=forms.HiddenInput(attrs={'class': 'form-control'}))

    def clean_id(self):
        data = self.cleaned_data['id']
        if not data:
            raise forms.ValidationError('Неверный ввод')
        else:
            return data
