from django.shortcuts import HttpResponse
from .models import DataFromAvtomat
from avtomat.models import Avtomat
import md5


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
            return HttpResponse()
