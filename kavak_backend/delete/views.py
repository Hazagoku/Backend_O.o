from django.shortcuts import render, HttpResponse
from cars.models import Car
from cars.models import Car_info
from users.models import User
import sys


def indexpage(request):
    ##Llama a la pagina con el formulario prototipo
    return render(request, 'formulario_delete.html')





def eliminar(request):
    #Coloca los datos en la base de datos
    ci = int(request.GET["car_id"])
    try:
        carid = Car.objects.get( car_id = ci)
    except Exception as e:
        return HttpResponse("Indice incorrecto")    
    Car.objects.filter(car_id=ci).delete()
    return HttpResponse("Eliminado de BD")