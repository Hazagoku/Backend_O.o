from django.db import models
from django import forms

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length = 254) 
    address = models.CharField(max_length=254)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)

