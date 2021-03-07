from django.db import models
from cars import models as modelsc
from users import models as modelsu

# Create your models here.
class Favorite(models.Model):
    car_id = models.ForeignKey(modelsc.Car, on_delete=models.CASCADE)
    user_id = models.ForeignKey(modelsu.User, on_delete=models.CASCADE)