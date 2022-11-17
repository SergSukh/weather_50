from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('weather.urls'), name='weather'),
    path('admin/', admin.site.urls),
]
