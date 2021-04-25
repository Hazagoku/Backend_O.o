
from django.contrib import admin
from django.urls import path
from filter import views  as filter_views

urlpatterns = [
    path('filter/', filter_views.form),
]
