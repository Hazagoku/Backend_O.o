from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse
from .models import User

import sys



def agregar(request):
    #Coloca los datos en la base de datos
    nombre = request.POST.get("name")
    apellido = request.POST.get("lastname")
    correo = request.POST.get("email")
    direccion = request.POST.get("address")
    #clave = request.POST.get("pass")
    BDG = User(name = nombre ,lastname = apellido, email = correo , address = direccion)
    BDG.save()
    return HttpResponse("Usuario agregado exitosamente")


def index(request):
    ##Llama a la pagina con el formulario prototipo
    return render(request, 'formulario_usuario.html')