from django.shortcuts import get_object_or_404, render

from .models import City, Weather


def index(request):
    city_list = Weather.objects.all()[:50]
    context ={
        'city_list': city_list
    }
    return render(request, 'cityes/index.html', context)
