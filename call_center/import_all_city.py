import csv
import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'call_center.settings')
django.setup()
from weather.models import City

path = 'call_center/data/'
os.chdir(path)


with open('csvData.csv', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=['rank', 'city', 'country', 'pop2022'])
    city = (City(
        name=_['city'],
        state=_['country'],
        population=_['pop2022']
    ) for _ in reader)
    City.objects.bulk_create(city)
