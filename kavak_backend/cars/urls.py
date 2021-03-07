
from django.contrib import admin
from django.urls import path
from cars import views  as car_views

urlpatterns = [
    path('cars/', car_views.indexpage),
    path('cars/r',car_views.guardar),
    path('lista_car', car_views.lista_car, name='lista_car')
]
