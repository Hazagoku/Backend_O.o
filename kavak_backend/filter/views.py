from cars.models import Car
from cars.models import Car_info

from rest_framework.decorators import api_view
import sys
import json
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
# Create your views here.
def valido(param):
    return param != '' and param is not None



def valido(param):
    return param != '' and param is not None

@api_view(["GET"])
def form(request):
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