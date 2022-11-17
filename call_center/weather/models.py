import time as t

from django.db import models

CLOUD = {
    0: 'Ясно',
    1: 'Редкие облака',
    2: 'Переменная облачность',
    3: 'Переменная облачность',
    4: 'Переменная облачность',
    5: 'Переменная облачность',
    6: 'Облачно с прояснениями',
    7: 'Облачно с прояснениями',
    8: 'Облачно с прояснениями',
    9: 'Облачно',
    10: 'Пасмурнно',
}


class City(models.Model):
    """Модель город."""
    name = models.CharField('Город', max_length=50)
    state = models.CharField('Страна', max_length=50)
    population = models.IntegerField('Население')

    class Meta:
        ordering = ['-population']

    def __str__(self) -> str:
        return f'{self.name}'


class Cloud(models.Model):
    """Модель облачности индекс, возвращает текст из словаря"""
    index = models.IntegerField('Индекс Облачности')

    def __str__(self) -> str:
        return f'{CLOUD[self.index//10]}'


class Wind(models.Model):
    """Модель ветер"""
    speed = models.FloatField('Скорость ветра')
    deg = models.IntegerField('Направление')

    def __str__(self) -> str:
        if self.deg > 23 and self.deg < 68:
            deg = 'СВ'
        elif self.deg >= 68 and self.deg < 112:
            deg = 'B'
        elif self.deg >= 112 and self.deg < 157:
            deg = 'ЮВ'
        elif self.deg >= 157 and self.deg < 202:
            deg = 'Ю'
        elif self.deg >= 202 and self.deg < 247:
            deg = 'ЮЗ'
        elif self.deg >= 247 and self.deg < 292:
            deg = 'З'
        elif self.deg >= 292 and self.deg < 337:
            deg = 'СЗ'
        else:
            deg = 'C'
        return f'{deg} {self.speed} м/с'


class Temp(models.Model):
    """Модель температуры"""
    temp = models.FloatField('Температура')
    feels_like = models.FloatField('Ощущается')
    temp_min = models.FloatField('Мин Температура')
    temp_max = models.FloatField('Макс Температура')

    def __str__(self) -> str:
        return f'{self.temp}'


class Weather(models.Model):
    """Модель погоды."""
    city = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name='weather'
    )
    timestamp = models.IntegerField('Время обновления')
    temp = models.ForeignKey(
        Temp, on_delete=models.CASCADE, related_name='weather_temp'
    )
    wind = models.ForeignKey(
        Wind, on_delete=models.CASCADE, related_name='weather_wind'
    )
    cloud = models.ForeignKey(
        Cloud, on_delete=models.CASCADE, related_name='cloud'
    )
    preassure = models.IntegerField('Давление')
    humidity = models.IntegerField('Влажность')

    class Meta:
        ordering = ['-timestamp']

    def date_time(self):
        dt = t.strftime(
            "%a, %d %b %Y %H:%M:%S +0000", t.localtime(self.timestamp)
        )
        return f'{dt}'
