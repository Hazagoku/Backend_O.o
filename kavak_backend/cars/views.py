from django.shortcuts import render, HttpResponse
from .models import Car
from .models import Car_info
from users.models import User
import sys




def guardar(request):
    #Coloca los datos en la base de datos
    us = request.POST.get("user_id")
    ciudad = request.POST.get("ciudad")
    locacion = request.POST.get("locacion")
    km = request.POST.get("km")
    color = request.POST.get("color")
    precio = request.POST.get("precio")
    car_infid = request.POST.get("car_infid")
    marca = request.POST.get("marca")
    modelo = request.POST.get("modelo")
    anio = request.POST.get("anio")
   
    
    try:
        ci = carinf_type = Car_info.objects.get( model = modelo )
        ui = User.objects.get( id =  us  )        
    except Exception as e:
        return HttpResponse("Indice incorrecto")    

    BDG = Car(user_id = ui ,status = "Disponible",city = ciudad ,location = locacion ,km = km , color = color , price = precio, carinfo_id = ci, year_purch = anio)
    BDG.save()
    return HttpResponse("guardado en BD")




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
            a = "user_id = " + str(x.user_id) + "<br>" + "status = " + x.status + "<br>" + "city = " + x.city + "<br>" + "location = " + x.location + "<br>" 
            b = "km = "  + str(x.km) + "<br>" + "color = " + x.color + "<br>" + "price = " + str(x.price) + "<br>" + "car_infid = " + str(x.carinfo_id_id) + "<br>" 
            c = "brand = " + cii.brand + "<br>" + "model = " + cii.model + "<br>" + "year = " + str(x.year_purch)
            e = a + b + c  + "<br>" + "<br>"
            d = d + e

        return HttpResponse(d)
    else:
        try:
            # Prototipo temporal de como sacar los datos de la BD
            ci = Car.objects.get( car_id = indice )
            cii = Car_info.objects.get( id = ci.carinfo_id_id )
            a = "user_id = " + str(ci.user_id) + "<br>" + "status = " + ci.status + "<br>" + "city = " + ci.city + "<br>" + "location = " + ci.location + "<br>" 
            b = "km = "  + str(ci.km) + "<br>" + "color = " + ci.color + "<br>" + "price = " + str(ci.price) + "<br>" + "car_infid = " + str(ci.carinfo_id_id) + "<br>" 
            c = "brand = " + cii.brand + "<br>" + "model = " + cii.model + "<br>" + "year = " + str(ci.year_purch)
            d = a + b + c
            return HttpResponse( d )
        except Exception as e:
            return HttpResponse("indice no encontrado")
    