import os

import requests
from django.core.management.base import BaseCommand
from dotenv import load_dotenv

from ...models import City, Cloud, Temp, Weather, Wind

load_dotenv()

API = os.getenv('API')
URL = 'https://api.openweathermap.org/data/2.5/weather'


class Command(BaseCommand):
    help = 'downloading weather in the 50 largest cities in the world'

    def handle(self, *args, **options):
        cityes = City.objects.all()[:50]
        for city in cityes:
            data = {
                'q': city.name,
                'units': 'metric',
                'appid': API
            }

            try:
                resp = requests.get(URL, params=data).json()
            except Exception as e:
                print(e)
            temp = Temp.objects.get_or_create(
                temp=resp['main']['temp'],
                feels_like=resp['main']['feels_like'],
                temp_min=resp['main']['temp_min'],
                temp_max=resp['main']['temp_max'],
            )
            cloud = Cloud.objects.get_or_create(
                index=resp['clouds']['all']
            )
            wind = Wind.objects.get_or_create(
                speed=resp['wind']['speed'],
                deg=resp['wind']['deg']
            )
            Weather.objects.create(
                city=city,
                timestamp=resp['dt'],
                temp=temp[0],
                wind=wind[0],
                cloud=cloud[0],
                preassure=resp['main']['pressure'],
                humidity=resp['main']['humidity']
            )
