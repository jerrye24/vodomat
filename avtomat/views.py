from django.shortcuts import render, redirect, reverse
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView
from .models import Avtomat, City, Street
from .forms import AvtomatForm


class AvtomatView(LoginRequiredMixin, ListView):
    queryset = Avtomat.objects.all().select_related('route').select_related('street__city')
    template_name = 'avtomat/avtomat.html'
    context_object_name = 'avtomat_table'


@login_required
def avtomat_form_view(request, pk):
    avtomat = Avtomat.objects.get(pk=pk)
    if request.method == 'POST':
        form = AvtomatForm(request.POST, instance=avtomat)
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
        form = AvtomatForm(instance=avtomat, initial = {'city': city, 'street_label': street_label})
        return render(request, 'avtomat/avtomat_form.html', {'form': form, 'avtomat': avtomat})


@login_required
def street_json_view(request):
    term = request.GET['term'].capitalize()
    city = request.GET['city']
    data = Street.objects.filter(city=city, street__startswith=term)
    streets = []
    for street in data:
        street = {'value': street.id, 'label': street.street}
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
