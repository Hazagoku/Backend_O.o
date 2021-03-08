from django.contrib import admin
from django.urls import path
from update import views  as update_views

urlpatterns = [
    path('update/', update_views.indexpage),
    path('update/elegir',update_views.elegir),
    path('update/editar',update_views.editar)

]
