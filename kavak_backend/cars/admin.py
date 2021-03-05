from django.contrib import admin
from cars import models 

# Register your models here.
admin.site.register(models.Car_info)
admin.site.register(models.Car)
