from django.shortcuts import render, HttpResponse
from cars.models import Car
from cars.models import Car_info
from users.models import User
import sys



def indexpage(request):
    ##Llama a la pagina con el formulario prototipo
    return render(request, 'formulario_elegir.html')

def elegir(request):
    #Coloca los datos en la base de datos
    ci = int(request.GET["car_id"])
    try:
        carid = Car.objects.get( car_id = ci)
        carinfoid = Car_info.objects.get( id = carid.carinfo_id_id )
    except Exception as e:
        return HttpResponse("Indice incorrecto")    
    return render(request, "formulario_update.html", {'carid': carid})



def editar(request):
    #Coloca los datos en la base de datos
    cai = int(request.GET["car_id"])
    ciudad = request.GET["ciudad"]
    locacion = request.GET["locacion"]
    km = request.GET["km"]
    color = request.GET["color"]
    precio = request.GET["precio"]
    car_infid = request.GET["car_infid"]
    marca = request.GET["marca"]
    modelo = request.GET["modelo"]
    anio = request.GET["anio"]
    try:
        ci = Car.objects.get( car_id = cai)  
        ci2 = carinf_type = Car_info.objects.get( model = modelo )
    except Exception as e:
        return HttpResponse("Error")    

    Car.objects.filter(car_id=cai).update(status = "Disponible",city = ciudad ,location = locacion ,km = km , color = color , price = precio, carinfo_id = ci2, year_purch = anio)
    return HttpResponse("Actualizado en BD")







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
    