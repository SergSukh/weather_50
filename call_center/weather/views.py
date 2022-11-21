from django.shortcuts import render

from .models import Weather


def index(request):
    city_list = Weather.objects.all()[:50]
    context = {
        'city_list': city_list
    }
    return render(request, 'cityes/index.html', context)
