from django.db import models
from django import forms
from cars import models as modelsc
from users import models as modelsu

# Create your models here.
class User(models.Model):
    user_id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length = 254) 
    address = models.CharField(max_length=254)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)

class Favorite(models.Model):
    favorite_id = models.IntegerField(primary_key = True)
    car_id = models.ForeignKey(modelsc.Car, on_delete=models.CASCADE)
    user_id = models.ForeignKey(modelsu.User, on_delete=models.CASCADE)