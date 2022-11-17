from django.contrib import admin

from .models import City, Temp, Weather


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'state', 'population']
    search_fields = ['name', 'state']


@admin.register(Weather)
class WeatherAdmin(admin.ModelAdmin):
    list_display = ['city', 'timestamp', 'temp', 'wind', 'cloud', 'preassure', 'humidity']
    search_fields = ['city']
