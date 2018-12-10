# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.utils.http import urlencode
from datetime import datetime
from statistic.models import Statistic
from avtomat.models import Avtomat


@login_required
def reports(request):
    return render(request, 'reports/reports.html')


@login_required
def billiards_activity_form(request):
    if request.method == 'POST':
        form = {
            'date': request.POST.get('date'),
            'start_period': request.POST.get('start_period'),
            'end_period': request.POST.get('end_period'),
            'amount': request.POST.get('amount')
        }
        return redirect(reverse('billiards_activity') + '?' + urlencode(form))
    else:
        return redirect('reports')


@login_required
def billiards_activity(request):
    date = datetime.strptime(request.GET.get('date'), '%Y-%m-%d').date()
    start_period = datetime.strptime(request.GET.get('start_period'), '%H:%M').time()
    end_period = datetime.strptime(request.GET.get('end_period'), '%H:%M').time()
    amount = int(request.GET.get('amount'))
    avtomats = Avtomat.objects.all().select_related('street', 'street__city')
    statistics = Statistic.objects.filter(time__range=(datetime.combine(date, start_period),
                                                       datetime.combine(date, end_period)))
    billiards_without_activity = []
    for avtomat in avtomats:
        statistic_from_avtomat = statistics.filter(avtomat_id=avtomat.id).only('grn', 'event')
        if statistic_from_avtomat:
            first = statistic_from_avtomat.first().grn
            amount_accepted = 0
            for i in statistic_from_avtomat:
                if i.event == 3:
                    continue
                if first < i.grn:
                    first = i.grn
                amount_accepted += first - i.grn
                first = i.grn
                if amount_accepted > amount:
                    break
            if amount_accepted <= amount:
                billiards_without_activity.append((avtomat, amount_accepted))
    return render(request, 'reports/billiards_activity.html', {'billiards_without_activity': billiards_without_activity,
                                                               'start_period': datetime.combine(date, start_period),
                                                               'end_period': datetime.combine(date, end_period),
                                                               'count': len(billiards_without_activity)})


@login_required
def coins_activity_form(request):
    if request.method == 'POST':
        form = {
            'date': request.POST.get('date'),
            'start_period': request.POST.get('start_period'),
            'end_period': request.POST.get('end_period'),
            'amount': request.POST.get('amount')
        }
        return redirect(reverse('coins_activity') + '?' + urlencode(form))
    else:
        return redirect('reports')


@login_required
def coins_activity(request):
    date = datetime.strptime(request.GET.get('date'), '%Y-%m-%d').date()
    start_period = datetime.strptime(request.GET.get('start_period'), '%H:%M').time()
    end_period = datetime.strptime(request.GET.get('end_period'), '%H:%M').time()
    amount = int(request.GET.get('amount'))
    avtomats = Avtomat.objects.all().select_related('street', 'street__city')
    statistics = Statistic.objects.filter(time__range=(datetime.combine(date, start_period),
                                                       datetime.combine(date, end_period)))
    coins_without_activity = []
    for avtomat in avtomats:
        statistic_from_avtomat = statistics.filter(avtomat_id=avtomat.id).only('kop', 'event')
        if statistic_from_avtomat:
            first = statistic_from_avtomat.first().kop
            amount_accepted = 0
            for i in statistic_from_avtomat:
                if i.event == 3:
                    continue
                if first < i.kop:
                    first = i.kop
                amount_accepted += first - i.kop
                first = i.kop
                if amount_accepted > amount:
                    break
            if amount_accepted <= amount:
                coins_without_activity.append((avtomat, amount_accepted))
    return render(request, 'reports/coins_activity.html', {'coins_without_activity': coins_without_activity,
                                                           'start_period': datetime.combine(date, start_period),
                                                           'end_period': datetime.combine(date, end_period),
                                                           'count': len(coins_without_activity)})