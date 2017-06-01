from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
import pygal
from pygal.style import Style
import datetime
from .models import Status
from avtomat.models import Avtomat
from collection.models import Collection
from statistic.models import Statistic


class StatusView(LoginRequiredMixin, ListView):
    queryset = Status.objects.all()
    template_name = 'status/status.html'
    context_object_name = 'status_table'


class StatusAlphabetView(LoginRequiredMixin, ListView):
    template_name = 'status/status.html'
    context_object_name = 'status_table'

    def get_queryset(self):
        return Status.objects.filter(avtomat__street__street__istartswith=self.args[0]).select_related('avtomat')


@login_required
def status_detail_view(request, id):
    date = datetime.date.today()
    avtomat = Avtomat.objects.get(id=id)
    status = Status.objects.get(avtomat=id)
    collections = Collection.objects.filter(avtomat=id, time__date=date)
    statistic = Statistic.objects.filter(avtomat=id, time__date=date).values_list('water_balance', flat=True)
    custom_style_water = Style(colors=('#79aec8',), font_family='Roboto')
    hist_water = pygal.Line(height=300, show_y_guides=False, show_legend=False, margin=0, style=custom_style_water,
                            dots_size=1)
    hist_water.add('Water', statistic.reverse())
    if avtomat.size:
        balance = int(status.water_balance / avtomat.size * 100)
    else:
        balance = 0
    return render(request, 'status/status_detail.html', {'avtomat': avtomat, 'status': status, 'date': date,
                                                         'collections': collections,
                                                         'hist_water': hist_water.render_data_uri(),
                                                         'balance': balance})


@login_required
def status_map_view(request):
    status = Status.objects.all().select_related('avtomat')
    return render(request, 'status/map_google.html', {'status': status})
