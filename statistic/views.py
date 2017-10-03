from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import StatisticForm
from .models import Statistic
from avtomat.models import Avtomat
import datetime


@login_required
def statistic_form_view(request):
    if request.method == 'POST':
        form = StatisticForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            period = data['period']
            start = period[0]
            try:
                end = period[1]
            except ImportError:
                end = start
            return redirect('statistic', start=start, end=end, id=data['id'])
    else:
        form = StatisticForm()
    return render(request, 'statistic/statistic_form.html', {'form': form})


@login_required
def statistic_view(request, start, end, id):
    start = datetime.date(int(start[4:]), int(start[2:4]), int(start[:2]))
    end = datetime.datetime(int(end[4:]), int(end[2:4]), int(end[:2]), 23, 59)
    statistic_table = Statistic.objects.filter(avtomat=id, time__range=(start, end))
    avtomat = Avtomat.objects.get(id=id)
    return render(request, 'statistic/statistic.html', {'statistic_table': statistic_table, 'start': start,
                                                        'end': end, 'avtomat': avtomat})
