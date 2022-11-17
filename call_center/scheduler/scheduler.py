import logging
import os
import sys

import requests
from apscheduler.schedulers.background import BackgroundScheduler
from django.conf import settings
from django_apscheduler.jobstores import register_events
from dotenv import load_dotenv
from weather.models import City, Cloud, Temp, Weather, Wind

load_dotenv()

scheduler = BackgroundScheduler(settings.SCHEDULER_CONFIG)

API = os.getenv('API')
URL = 'https://api.openweathermap.org/data/2.5/weather'


def get_weather_city():
    """Функция регулярного обновления информации о погоде."""
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


def start():
    if settings.DEBUG:
        logging.basicConfig()
        logging.getLogger('apscheduler').setLevel(logging.DEBUG)
    register_events(scheduler)
    scheduler.start()
    print("Scheduler started...", file=sys.stdout)
