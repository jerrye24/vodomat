from django.shortcuts import render, redirect
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
from route.models import Route


class StatusView(LoginRequiredMixin, ListView):
    queryset = Status.objects.all()
    template_name = 'status/status.html'
    context_object_name = 'status_table'

    def get_context_data(self, **kwargs):
        context = super(StatusView, self).get_context_data(**kwargs)
        context['routes'] = Route.objects.all()
        context['status_count'] = Status.objects.count()
        return context

    def get_queryset(self):
        route = self.request.GET.get('route')
        if route:
            return Status.objects.filter(avtomat__route__route_number=route).order_by('avtomat')
        else:
            return Status.objects.all().select_related('avtomat__street', 'avtomat__street__city')


@login_required
def status_search_form(request):
    avtomat_id = request.POST.get('id')
    if avtomat_id:
        return redirect('status_detail', id=avtomat_id)
    else:
        return redirect('status')


class StatusAlphabetView(LoginRequiredMixin, ListView):
    template_name = 'status/status.html'
    context_object_name = 'status_table'

    def get_queryset(self):
        return Status.objects.filter(avtomat__street__street__istartswith=self.args[0]).select_related('avtomat__street', 'avtomat__street__city')


@login_required
def status_detail_view(request, id):
    today = datetime.date.today()
    one_day_ago = today - datetime.timedelta(days=1)
    two_days_ago = today - datetime.timedelta(days=2)
    avtomat = Avtomat.objects.get(id=id)
    status = Status.objects.get(avtomat=id)
    collections = Collection.objects.filter(avtomat=id, time__date=today)
    statistic = Statistic.objects.filter(avtomat=id, time__gte=today).values_list('water_balance', flat=True)
    custom_style_water = Style(colors=('#79aec8',), font_family='Roboto')
    hist_water = pygal.Line(height=300, show_y_guides=False, show_legend=False, margin=0, style=custom_style_water,
                            dots_size=1)
    hist_water.add('Water', statistic.reverse())
    if avtomat.size:
        balance = int(status.water_balance / avtomat.size * 100)
    else:
        balance = 0
    return render(request, 'status/status_detail.html', {'avtomat': avtomat, 'status': status, 'today': today,
                                                         'one_day_ago': one_day_ago,
                                                         'two_days_ago': two_days_ago,
                                                         'collections': collections,
                                                         'hist_water': hist_water.render_data_uri(),
                                                         'balance': balance})


@login_required
def status_map_view(request):
    status = Status.objects.all().select_related('avtomat__street', 'avtomat__street__city')
    return render(request, 'status/map_google.html', {'status': status})
