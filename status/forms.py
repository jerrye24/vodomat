# coding=utf-8
from django import forms

class ErrorForm(forms.Form):

    ERRORS = (
        ('ev_water', 'Вода'),
        ('ev_volt', 'Сеть'),
        ('ev_counter', 'Счетчик'),
        ('ev_register', 'Регистратор'),
        ('ev_bill', 'Купюрник'),
    )

    errors = forms.ChoiceField(widget=forms.RadioSelect, choices=ERRORS)