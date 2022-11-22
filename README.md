# weather_50
Сервис архива погоды в 50 крупнейщих городах мира по численности населения.
Источник данных о погоде API:
- 'https://api.openweathermap.org/data/2.5/weather'
Источник городов и населения:
- https://worldpopulationreview.com/

Информация хранится в моделях:
- City(Модель город) сортировка по количеству населения
- Cloud(Облачность) количество вариантов ограниченно, приведет к сохранению места в БД
- Wind(Ветер) количество вариантов ограниченно, приведет к сохранению места в БД
- Temp(Температура)
- Weather(Погода) сортировка в порядке обновления(последнее обновление первым)

### Для развертывания проекта на локальной машине:
- клонируйте проект: git clone git@github.com:SergSukh/weather_50.git
- создайте файл <.env> в папке infra/
- запишите в файл: SECRET_KEY=(secret key django app), DEBUG, DB_ENGINE, DB_NAME, POSTGRES_USER, POSTGRES_PASSWORD, DB_HOST, DB_PORT, API(weather API key)
- выполните команду $ docker-compose up -d из папки imfra
- выполните миграции $ docker-compose exec -T web python manage.py migrate
- выполните работу по сбору статики docker-compose exec -T web python manage.py collectstatic --noinput
- запустите команду $ docker-compose exec -T web python import_all_city.py (наполнит базу городами, установит расписание обновления)


### Установка Docker: <a href=https://docs.docker.com/engine/install/ubuntu/>docker</a>

# Работа над проектом: Сергей Суханов
### Стек технологий: Python3, Django4 ООП, PostgreSQL, GIT, import csv, APScheduler, Docker

библиотека APScheduler выбрана т.к. нет необходимости передавать какую либо информацию в запрос, длительность и исполнение расписание легко контролируется из админки
- 
