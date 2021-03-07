from django.db import models
from cars import models as modelsc
from users import models as modelsu

# Create your models here.
class Venta(models.Model):
    car_id = models.ForeignKey(modelsc.Car, on_delete=models.CASCADE)
    date = models.DateField()
    user_id = models.ForeignKey(modelsu.User, on_delete=models.CASCADE)

class Compra(models.Model):
    user_id = models.ForeignKey(modelsu.User, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.FloatField()
    car_id = models.ForeignKey(modelsc.Car, on_delete=models.CASCADE)