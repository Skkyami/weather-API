from .views import weather
from django.urls import path

urlpatterns = [
    path('weather/', weather),
]
