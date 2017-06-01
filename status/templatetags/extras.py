# coding=utf-8
from django import template

register = template.Library()


# Фильтр расшифровка принятых событий
@register.filter
def event(number):
    switch = {
        1: 'нет воды',
        2: 'нет питания',
        3: 'инкассация',
        4: 'удар',
        5: 'мало воды',
        6: 'отправка данных',
        7: 'купюроприемник',
        8: 'регистратор',
        9: 'вкл автомата',
        10: 'сервис вкл',
        11: 'сервис выкл',
        12: 'сервисное вскрытие',
        13: '12 часов',
    }
    return switch.get(number, 'error')
