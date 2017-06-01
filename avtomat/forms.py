# coding=utf-8
from .models import Avtomat, City
from django import forms


class UIWidget(forms.TextInput):
    class Media:
        css = {'all': ('//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css', )}
        js = ('https://code.jquery.com/ui/1.12.1/jquery-ui.js', )


class AvtomatForm(forms.ModelForm):

    city = forms.ModelChoiceField(queryset=City.objects.all(), label=u'Город')
    street_label = forms.CharField(widget=UIWidget, max_length=50, label=u'Улица')

    class Meta:
        model = Avtomat
        fields = ['city', 'street_label', 'street', 'house', 'route', 'water_price', 'size', 'phone', 'register', 'security', 'competitors']
        widgets = {'street': forms.HiddenInput}
