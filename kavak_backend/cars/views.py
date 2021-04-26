import json
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.http import Http404

#Modelos
from cars.models import Car
from cars.models import Car_info
from users.models import User

from rest_framework.decorators import api_view
import sys
import json

def listing(request):
    car_list = Car.objects.all()
    paginator = Paginator(car_list, 2) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'pagination.html', {'page_obj': page_obj})

#Listado de vehiculos y paginacion
def car_list(request):
    car = Car.objects.all()
    page = request.GET.get('page', 1)
    
    try:
        paginator = Paginator(car,2)
        car = paginator.page(page)
    except:
        raise Http404

    contexto = {
        'entity': car,
        'paginator': paginator
     }
    return render(request, 'list.html', contexto)


@api_view(["POST"])
def guardar(request):
    #Coloca los datos en la base de datos
    us = request.POST.get("user_id")
    ciudad = request.POST.get("ciudad")
    locacion = request.POST.get("locacion")
    km = request.POST.get("km")
    color = request.POST.get("color")
    precio = request.POST.get("precio")
    car_infid = request.POST.get("car_infid")
    marca =   request.POST.get("marca")
    modelo = request.POST.get("modelo") 
    anio = request.POST.get("anio")
    print( request )
    sys.stdout.flush()

    try:
        ci = carinf_type = Car_info.objects.get( model = modelo )
        ui = User.objects.get( id =  us  )        
    except Exception as e:
        return HttpResponse("Indice incorrecto")

    if request.method == "POST":
        BDG = Car(user_id = ui ,status = "Disponible",city = ciudad ,location = locacion ,km = km , color = color , price = precio, carinfo_id = ci, year_purch = anio)
        BDG.save()
        return HttpResponse("guardado en BD")

@api_view(["GET"])
def extraer_datos(request):
    data = []
    carros = Car.objects.all()

    for x in carros:
        cii = Car_info.objects.get( id = x.carinfo_id_id )
        dt = {
            "car_id" : str(x.car_id),
            "km" : str(x.km),
            "color" : str(x.color),
            "brand" :  str(cii.brand),
            "model" : str(cii.model),
            "year" : str(x.year_purch)
        }
        data.append(dt)
        
    return JsonResponse(data, safe = False)


def prueba(request):
    ##Llama a la pagina con el formulario prototipo
    return HttpResponse("Soy la pantalla principal del backend")

def indexpage(request):
    ##Llama a la pagina con el formulario prototipo
    return render(request, 'home.html')


def lista_car(request):
    indice = int(request.GET["Numero"])
    if indice == 0:         
        d = "Impresion prototipo:" + "<br></br>"
        carros = Car.objects.all()
        
        data
        
        
        for x in carros:
            cii = Car_info.objects.get( id = x.carinfo_id_id )
            carid = "car_id = " + str(x.car_id) + "<br>"
            a = "user_id = " + str(x.user_id) + "<br>" + "status = " + x.status + "<br>" + "city = " + x.city + "<br>" + "location = " + x.location + "<br>" 
            b = "km = "  + str(x.km) + "<br>" + "color = " + x.color + "<br>" + "price = " + str(x.price) + "<br>" + "car_infid = " + str(x.carinfo_id_id) + "<br>" 
            c = "brand = " + cii.brand + "<br>" + "model = " + cii.model + "<br>" + "year = " + str(x.year_purch)
            e = a + b + c  + "<br>" + "<br>"
            d = d + carid + e

        return HttpResponse(d)
    else:
        try:
            # Prototipo temporal de como sacar los datos de la BD
            ci = Car.objects.get( car_id = indice )
            cii = Car_info.objects.get( id = ci.carinfo_id_id )
            carid = "car_id = " + str(ci.car_id) + "<br>"
            a = "user_id = " + str(ci.user_id) + "<br>" + "status = " + ci.status + "<br>" + "city = " + ci.city + "<br>" + "location = " + ci.location + "<br>" 
            b = "km = "  + str(ci.km) + "<br>" + "color = " + ci.color + "<br>" + "price = " + str(ci.price) + "<br>" + "car_infid = " + str(ci.carinfo_id_id) + "<br>" 
            c = "brand = " + cii.brand + "<br>" + "model = " + cii.model + "<br>" + "year = " + str(ci.year_purch)
            d = carid + a + b + c
            return HttpResponse( d )
        except Exception as e:
            return HttpResponse("indice no encontrado")

