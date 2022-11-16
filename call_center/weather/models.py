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
    name = models.CharField('Город', max_length=50)
    state = models.CharField('Страна', max_length=50)
    population = models.IntegerField('Население')

    class Meta:
        ordering = ['-population']

    def __str__(self) -> str:
        return f'{self.name}'


class Cloud(models.Model):
    index = models.IntegerField('Индекс Облачности')

    def __str__(self) -> str:
        return f'{CLOUD[self.index//10]}'


class Wind(models.Model):
    speed = models.FloatField('Скорость ветра')
    deg = models.IntegerField('Направление')


class Temp(models.Model):
    temp = models.FloatField('Температура')
    feels_like = models.FloatField('Ощущается')
    temp_min = models.FloatField('Мин Температура')
    temp_max = models.FloatField('Макс Температура')

    def __str__(self) -> str:
        return f'{self.temp}'


class Weather(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    timestamp = models.IntegerField('Время обновления')
    temp = models.ForeignKey(Temp, on_delete=models.CASCADE)
    wind = models.ForeignKey(Wind, on_delete=models.CASCADE)
    cloud = models.ForeignKey(Cloud, on_delete=models.CASCADE)
    preasure = models.IntegerField('Давление')
    humidity = models.IntegerField('Влажность')

    class Meta:
        ordering = ['-timestamp']