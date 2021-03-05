from django.db import models

# Create your models here.
class Car_info(models.Model):
    transmission = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    traction = models.CharField(max_length=100)
    hpower = models.CharField(max_length=100)
    motor = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    fuel = models.CharField(max_length=100)
    year = models.IntegerField()

class Cars(models.Model):
    car_id = models.AutoField(primary_key = True) 
    status = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    location  = models.CharField(max_length=100)
    km  = models.IntegerField()
    color = models.CharField(max_length=100)
    price = models.FloatField()
    carinfo_id = models.ForeignKey(Car_info, on_delete=models.CASCADE)