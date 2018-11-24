from django.shortcuts import render, redirect, reverse
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView
from .models import Avtomat, City, Street
from .forms import AvtomatForm


class AvtomatView(LoginRequiredMixin, ListView):
    queryset = Avtomat.objects.all().select_related('route', 'street__city')
    template_name = 'avtomat/avtomat.html'
    context_object_name = 'avtomat_table'


class AvtomatAlphabetView(LoginRequiredMixin, ListView):
    template_name = 'avtomat/avtomat.html'
    context_object_name = 'avtomat_table'

    def get_queryset(self):
        return Avtomat.objects.filter(street__street__istartswith=self.args[0]).select_related('route', 'street__city')


@login_required
def avtomat_form_view(request, pk):
    avtomat = Avtomat.objects.get(pk=pk)
    if request.method == 'POST':
        form = AvtomatForm(request.POST)
        if form.is_valid():
            form = AvtomatForm(request.POST, instance=avtomat)
            form.save()
#            if not avtomat.latitude or not avtomat.longitude:
#                return redirect('/avtomat/' + '?number=%s' % avtomat.number)
#            else:
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
        form = AvtomatForm(instance=avtomat, initial={'city': city, 'street_label': street_label})
        return render(request, 'avtomat/avtomat_form.html', {'form': form, 'avtomat': avtomat})


@login_required
def street_json_view(request):
    term = request.GET['term'].capitalize()
    city = request.GET['city']
    data = Street.objects.filter(city=city, street__startswith=term)
    streets = []
    for street in data:
        street = {'id': street.id, 'label': street.street}
        streets.append(street)
    return JsonResponse(streets, safe=False)


class StreetView(LoginRequiredMixin, ListView):
    queryset = Street.objects.all().select_related('city')
    template_name = 'avtomat/street.html'
    context_object_name = 'street_table'


class StreetCreateView(LoginRequiredMixin, CreateView):
    model = Street
    fields = ['city', 'street']
    template_name = 'avtomat/street_create.html'

    def get_success_url(self):
        return reverse('street')


class StreetEditView(LoginRequiredMixin, UpdateView):
    model = Street
    fields = ['city', 'street']
    template_name = 'avtomat/street_edit.html'

    def get_success_url(self):
        return reverse('street')


class CityView(LoginRequiredMixin, ListView):
    model = City
    template_name = 'avtomat/city.html'
    context_object_name = 'city_table'


class CityCreateView(LoginRequiredMixin, CreateView):
    model = City
    fields = ['city', ]
    template_name = 'avtomat/city_create.html'

    def get_success_url(self):
        return reverse('city')


class CityEditView(LoginRequiredMixin, UpdateView):
    model = City
    fields = ['city', ]
    template_name = 'avtomat/city_edit.html'

    def get_success_url(self):
        return reverse('city')


@login_required
def avtomat_json_view(request):
    term = request.GET.get('term').capitalize()
    data = Avtomat.objects.filter(street__street__startswith=term)
    avtomats = []
    for avtomat in data:
        avtomat = {'label': str(avtomat), 'id': avtomat.id}
        avtomats.append(avtomat)
    return JsonResponse(avtomats, safe=False)
