# coding: utf8
from vodomat.models import Avtomat, Status, Statistic, Collection, DataFromAvtomat, Route, City, Street
from vodomat.forms import *
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic.dates import DayArchiveView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse, JsonResponse
import md5
import pygal
from pygal.style import Style
import datetime
import calendar


def data_from_avtomat(request):
    password = md5.new(request.GET['pass']).hexdigest()
    if password == 'fdb7bc366f8e854fb470c944a8a70ba4':
        data = request.GET['data']
        line = DataFromAvtomat(line=data)
        line.save()
        number = data[:4]
        try:
            price = Avtomat.objects.get(number=number).water_price
            return HttpResponse('Price={:0>4}'.format(price))
        except:
            return HttpResponse('Ok')


@login_required
def status_view(request):
    status_table = Status.objects.all().select_related('avtomat')
    status_table_mobile = Status.objects.order_by('avtomat')
    browser = request.META['HTTP_USER_AGENT']
    if browser.find('Android') != -1:
        return render(request, 'vodomat/mobile.html', {'status_table_mobile': status_table_mobile})
    else:
        return render(request, 'vodomat/status.html', {'status_table': status_table})


class AvtomatView(LoginRequiredMixin, ListView):
    queryset = Avtomat.objects.all().select_related('route')
    template_name = 'vodomat/avtomat.html'
    context_object_name = 'avtomat_table'

@login_required
def street_json_view(request):
    term = request.GET['term'].capitalize()
    city = request.GET['city']
    data = Street.objects.filter(city=city, street__startswith=term)
    streets = []
    for street in data:
        street = {'value': street.id, 'label': street.street}
        streets.append(street)
    # streets = {street.id: street.street for street in data}
    return JsonResponse(streets, safe=False)


# class EditAvtomatView(LoginRequiredMixin, UpdateView):
#     model = Avtomat
#     fields = ['street', 'house', 'route', 'water_price', 'size', 'phone', 'register', 'security', 'competitors']
#     success_url = '/avtomat/'
#     template_name = 'vodomat/edit_avtomat.html'


@login_required
def edit_avtomat_form_view(request, pk):
    avtomat = Avtomat.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditAvtomatForm(request.POST, instance=avtomat)
        if form.is_valid():
            data = form.cleaned_data
            avtomat.street = data['street']
            avtomat.house = data['house']
            avtomat.route = data['route']
            avtomat.price = data['water_price']
            avtomat.size = data['size']
            avtomat.phone = data['phone']
            avtomat.register = data['register']
            avtomat.security = data['security']
            avtomat.competitors = data['competitors']
            avtomat.save()
            return redirect('avtomat')
    else:
        try:
            city = avtomat.street.city
        except AttributeError:
            city = u''
        try:
            street_label = avtomat.street.street
        except AttributeError:
            street_label = u''
        form = EditAvtomatForm(instance=avtomat, initial={'city': city, 'street_label': street_label})
        return render(request, 'vodomat/edit_avtomat.html', {'form': form, 'avtomat': avtomat})


@login_required
def detail_avtomat_view(request, id):
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
    return render(request, 'vodomat/detail_avtomat.html', {'avtomat': avtomat, 'status': status, 'date': date,
                                                           'collections': collections,
                                                           'hist_water': hist_water.render_data_uri(),
                                                           'balance': balance})


class CollectionDayView(LoginRequiredMixin, DayArchiveView):
    queryset = Collection.objects.all().select_related('avtomat')
    date_field = 'time'
    template_name = 'vodomat/collection.html'
    context_object_name = 'collection_table'
    month_format = '%m'
    allow_empty = True
    allow_future = True


@login_required
def collection_route_view(request, year, month, day):
    previous_day = datetime.date(int(year), int(month), int(day)) - datetime.timedelta(days=1)
    next_day = datetime.date(int(year), int(month), int(day)) + datetime.timedelta(days=1)
    collection_route = []
    routs = Route.objects.all()
    for route in routs:
        collection_route.append([route, Collection.objects.filter(avtomat__route=route,
                                                                  time__date=datetime.date(int(year), int(month),
                                                                                           int(day))).select_related('avtomat')])
    return render(request, 'vodomat/collection_route.html', {'collection_route': collection_route,
                                                             'previous_day': previous_day, 'next_day': next_day,
                                                             'today': datetime.date(int(year), int(month), int(day))})


@login_required
def collection_missing_view(request):
    period = datetime.date.today() - datetime.timedelta(days=3)
    collections_of_period = Collection.objects.filter(time__gte=period).values_list('avtomat', flat=True)
    collection_missing_avtomats = Avtomat.objects.exclude(id__in=list(collections_of_period))
    return render(request, 'vodomat/collection_missing.html', {'collection_missing_avtomats': collection_missing_avtomats})


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
    return render(request, 'vodomat/period_form.html', {'form': form})


@login_required
def collection_period_view(request, start, end, id):
    start = datetime.date(int(start[4:]), int(start[2:4]), int(start[:2]))
    end = datetime.datetime(int(end[4:]), int(end[2:4]), int(end[:2]), 23, 59)
    collection_period = Collection.objects.filter(avtomat=id, time__range=(start, end)).select_related('avtomat')
    avtomat = Avtomat.objects.get(id=id)
    return render(request, 'vodomat/collection_period.html', {'collection_period': collection_period, 'start': start,
                                                              'end': end, 'avtomat': avtomat})


@login_required
def statistic_form_view(request):
    today = datetime.date.today()
    avtomat_list = Avtomat.objects.all()
    paginator = Paginator(avtomat_list, 15)
    page = request.GET.get('page')
    try:
        avtomat_list_paginator = paginator.page(page)
    except PageNotAnInteger:
        avtomat_list_paginator = paginator.page(1)
    except EmptyPage:
        avtomat_list_paginator = paginator.page(paginator.num_pages)
    if request.method == 'POST':
        form = StatisticForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if data['visualization']:
                return redirect('visualization', year=today.year, month=today.month, id=data['avtomat'].id)
            else:
                return redirect('statistic', year=today.year, month=today.month, day=today.day,
                                id=data['avtomat'].id)
    else:
        form = StatisticForm()
    return render(request, 'vodomat/statistic_form.html', {'form': form, 'avtomat_list': avtomat_list_paginator})


class StatisticDayView(LoginRequiredMixin, DayArchiveView):
    date_field = 'time'
    template_name = 'vodomat/statistic.html'
    context_object_name = 'statistic_table'
    month_format = '%m'
    allow_empty = True
    allow_future = True

    def get_queryset(self):
        return Statistic.objects.filter(avtomat=self.kwargs['id']).select_related('avtomat')

    def get_context_data(self, **kwargs):
        context = super(StatisticDayView, self).get_context_data(**kwargs)
        context['avtomat'] = Avtomat.objects.get(id=self.kwargs['id'])
        return context


@login_required
def statistic_period_form_view(request):
    if request.method == 'POST':
        form = PeriodForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            period = data['period']
            start = period[0]
            try:
                end = period[1]
            except ImportError:
                end = start
            return redirect('statistic_period', start=start, end=end, id=data['avtomat'].id)
    else:
        form = PeriodForm()
    return render(request, 'vodomat/period_form.html', {'form': form})


@login_required
def statistic_period_view(request, start, end, id):
    start = datetime.date(int(start[4:]), int(start[2:4]), int(start[:2]))
    end = datetime.datetime(int(end[4:]), int(end[2:4]), int(end[:2]), 23, 59)
    statistic_period = Statistic.objects.filter(avtomat=id, time__range=(start, end)).select_related('avtomat')
    avtomat = Avtomat.objects.get(id=id)
    return render(request, 'vodomat/statistic_period.html', {'statistic_period': statistic_period, 'start': start,
                                                             'end': end, 'avtomat': avtomat})


class SearchView(LoginRequiredMixin, ListView):
    template_name = 'vodomat/status.html'
    context_object_name = 'status_table'

    def get_queryset(self):
        return Status.objects.filter(avtomat__street__street__istartswith=self.args[0]).select_related('avtomat')


class RouteView(LoginRequiredMixin, ListView):
    model = Route
    template_name = 'vodomat/route.html'
    context_object_name = 'route_table'


class RouteListView(LoginRequiredMixin, ListView):
    model = Route
    template_name = 'vodomat/route_list.html'
    context_object_name = 'route_table'


class CreateRouteView(LoginRequiredMixin, CreateView):
    model = Route
    fields = ['route_number', 'car_number', 'driver']
    success_url = '/route/'
    template_name = 'vodomat/create_route.html'


class EditRouteView(LoginRequiredMixin, UpdateView):
    model = Route
    fields = ['route_number', 'car_number', 'driver']
    success_url = '/route/'
    template_name = 'vodomat/edit_route.html'


class RouteSortedView(LoginRequiredMixin, ListView):
    template_name = 'vodomat/status.html'
    context_object_name = 'status_table'

    def get_queryset(self):
        return Status.objects.filter(avtomat__route__route_number=self.kwargs['route']).select_related('avtomat')


@login_required
def delete_route_view(request, pk):
    Route.objects.get(id=pk).delete()
    return redirect('route')


@login_required
def visualization_view(request, year, month, id):
    water = []
    days = []
    avtomat = Avtomat.objects.get(id=id)
    date = datetime.date(int(year), int(month), day=1)
    for day in range(1, calendar.monthrange(int(year), int(month))[1] + 1):
        data = Statistic.objects.filter(avtomat=id, time__date=datetime.date(int(year), int(month), day))
        if data:
            money_last = data.latest('time').how_money
            money_first = data.earliest('time').how_money
            price = data[0].water_price
            collections = sum(data.filter(event=3).values_list('how_money', flat=True))
            if collections:
                money_today = money_last + collections - money_first
            else:
                money_today = money_last - money_first
            water.append(round(money_today / price, 1))
        else:
            water.append(0)
        days.append(day)
# Make histogram
    custom_style_water = Style(colors=('#79aec8', ), font_family='Roboto')
    hist_water = pygal.Bar(height=300, show_y_guides=False, show_legend=False, margin=0, style=custom_style_water,
                           print_values=True, print_values_position='top', print_zeroes=False)
    hist_water.x_labels = days
    hist_water.add('Water', water)
    next_month = int(month) + 1
    prev_month = int(month) - 1
    prev_year = next_year = year
    if prev_month == 0:
        prev_month = 12
        prev_year = int(year) - 1
    if next_month == 13:
        next_month = 1
        next_year = int(year) + 1
    return render(request, 'vodomat/visualization.html', {'hist_water': hist_water.render_data_uri(),
                                                          'prev_year': prev_year, 'next_year': next_year,
                                                          'prev_month': prev_month, 'next_month': next_month,
                                                          'avtomat': avtomat, 'date': date, 'water_month': sum(water)})


@login_required
def map_view(request):
    status = Status.objects.all().select_related('avtomat')
    return render(request, 'vodomat/map.html', {'status': status})


class StreetView(LoginRequiredMixin, ListView):
    model = Street
    template_name = 'vodomat/street.html'
    context_object_name = 'street_table'


class CreateStreetView(LoginRequiredMixin, CreateView):
    model = Street
    fields = ['city', 'street']
    success_url = '/street/'
    template_name = 'vodomat/create_street.html'


class EditStreetView(LoginRequiredMixin, UpdateView):
    model = Street
    fields = ['city', 'street']
    success_url = '/street/'
    template_name = 'vodomat/edit_street.html'


class CityView(LoginRequiredMixin, ListView):
    model = City
    template_name = 'vodomat/city.html'
    context_object_name = 'city_table'


class CreateCityView(LoginRequiredMixin, CreateView):
    model = City
    fields = ['city', ]
    success_url = '/city/'
    template_name = 'vodomat/create_city.html'


class EditCityView(LoginRequiredMixin, UpdateView):
    model = City
    fields = ['city', ]
    success_url = '/city/'
    template_name = 'vodomat/edit_city.html'


@login_required
def detail_mobile_view(request, number):
    detail = Status.objects.get(avtomat__number=number)
    try:
        collections = Collection.objects.filter(avtomat__number=number)[0]
    except Collection.DoesNotExist:
        collections = 0
    return render(request, 'vodomat/detail_mobile.html', {'detail': detail, 'collections': collections})
