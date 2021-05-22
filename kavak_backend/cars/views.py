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

def valido(param):
    return param != '' and param is not None

@api_view(["GET"])
def car_list(request):
    datos = []
    
    page = request.GET.get('page', 1)
    Carqs = Car.objects.all()
    query_min_precio = request.GET.get('precio_min')
    query_max_precio = request.GET.get('precio_max')
    query_min_kilo = request.GET.get('kil_min')
    query_max_kilo = request.GET.get('kil_max')
    query_modelo = request.GET.getlist('modelo')
    query_transmicion = request.GET.get('transmicion')
    query_marca = request.GET.getlist('marca')
    query_color = request.GET.getlist('color')
    query_ciudad = request.GET.getlist('ciudad')
    query_anio = request.GET.getlist('anio')
    query_tipo = request.GET.getlist('tipo')
    query_combustible = request.GET.getlist('combustible')
    query_estatus = request.GET.getlist('status')
    query_locacion = request.GET.getlist('locacion')

    if(valido(query_min_precio)):
        Carqs = Carqs.filter(price__gte=query_min_precio)
    if(valido(query_max_precio)):
        Carqs = Carqs.filter(price__lte=query_max_precio)
    if((query_modelo)):
        Carqs = Carqs.filter(carinfo_id__model__in =query_modelo)
    if(valido(query_transmicion) and query_transmicion != 'Todas'):
        Carqs = Carqs.filter(carinfo_id__transmission=query_transmicion)
    if((query_marca)):
        Carqs = Carqs.filter(carinfo_id__brand__in=query_marca)
    if((query_color)):
        Carqs = Carqs.filter(color__in=query_color)
    if(valido(query_min_kilo)):
        Carqs = Carqs.filter(km__gte=query_min_kilo)
    if(valido(query_max_kilo)):
        Carqs = Carqs.filter(km__lte=query_max_kilo)
    if((query_ciudad)):
        Carqs = Carqs.filter(city__in=query_ciudad)
    if((query_anio)):
        Carqs = Carqs.filter(year_purch__in=query_anio)
    if((query_tipo)):
        Carqs = Carqs.filter(carinfo_id__type__in=query_tipo)
    if((query_combustible)):
        Carqs = Carqs.filter(carinfo_id__fuel__in=query_combustible)
    if((query_estatus)):
        Carqs = Carqs.filter(status__in=query_estatus)
    if((query_locacion)):
        Carqs = Carqs.filter(location__in=query_locacion)

    for x in Carqs:
        cii = Car_info.objects.get( id = x.carinfo_id_id )
        dt = {
            "car_id" : str(x.car_id),
            "color" : str(x.color),
            "brand" :  str(cii.brand),
            "model" : str(cii.model),
            "year" : str(x.year_purch),
            "location" : str(x.location),
            "price" : str(x.price),
            "fuel" : str(cii.fuel),
            "transmission" : str(cii.transmission),
            "status" : str(x.status)

        }
        datos.append(dt)
    #return render(request, 'list.html', contexto)
    return JsonResponse(datos, safe = False)
    #http://127.0.0.1:8000/?page=1

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
            "num"   : len(carros),
            "year" : str(x.year_purch)
        }
        data.append(dt)
        
    return JsonResponse(data, safe = False)


@api_view(["GET"])
def extraer(request):
    data = []
    carros = Car.objects.all()
    dt = {
        "num" : len(carros)
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

