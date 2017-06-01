from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import DayArchiveView
from .models import Collection
from .forms import PeriodForm
from avtomat.models import Avtomat
import datetime


class CollectionDayView(LoginRequiredMixin, DayArchiveView):
    queryset = Collection.objects.all().select_related('avtomat')
    date_field = 'time'
    template_name = 'collection/collection_day.html'
    context_object_name = 'collection_table'
    month_format = '%m'
    allow_empty = True
    allow_future = True


@login_required
def collection_period_form_view(request):
    if request.method == 'POST':
        form = PeriodForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            period = data['period']
            start = period[0]
            try:
                end = period[1]
            except IndexError:
                end = start
            return redirect('collection_period', start=start, end=end, id=data['avtomat'].id)
    else:
        form = PeriodForm()
    return render(request, 'collection/period_form.html', {'form': form})


@login_required
def collection_period_view(request, start, end, id):
    start = datetime.date(int(start[4:]), int(start[2:4]), int(start[:2]))
    end = datetime.datetime(int(end[4:]), int(end[2:4]), int(end[:2]), 23, 59)
    collection_period = Collection.objects.filter(avtomat=id, time__range=(start, end)).select_related('avtomat')
    avtomat = Avtomat.objects.get(id=id)
    return render(request, 'collection/collection_period.html', {'collection_period': collection_period, 'start': start,
                                                              'end': end, 'avtomat': avtomat})