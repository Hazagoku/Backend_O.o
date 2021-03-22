from django.contrib import admin
from django.urls import path
from update import users  as users_views

urlpatterns = [
	path('users/', users_views.index),
    path('users/create_user', users_views.agregar)
]
