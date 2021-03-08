from django.contrib import admin
from django.urls import path
from delete import views  as delete_views

urlpatterns = [
    path('delete/', delete_views.indexpage),
    path('delete/r',delete_views.eliminar)
]
