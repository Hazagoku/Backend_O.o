from django.shortcuts import render
from cars.models import Car
from cars.models import Car_info

# Create your views here.
def valido(param):
    return param != '' and param is not None



def form(request):
	Carqs = Car.objects.all()
	Marcas = Car_info.objects.order_by('brand').values_list('brand', flat = True).distinct()
	Modelos = Car_info.objects.order_by('model').values_list('model', flat = True).distinct()
	Transmiciones = Car_info.objects.order_by('transmission').values_list('transmission', flat = True).distinct()
	Ciudad = Car.objects.order_by('city').values_list('city', flat = True).distinct()
	Anios = Car_info.objects.order_by('year').values_list('year', flat = True).distinct()
	Tipos = Car_info.objects.order_by('type').values_list('type', flat = True).distinct()
	Colores = Car.objects.order_by('color').values_list('color', flat = True).distinct()
	Combustibles = Car_info.objects.order_by('fuel').values_list('fuel', flat = True).distinct()
	Estatus = Car.objects.order_by('status').values_list('status', flat = True).distinct()

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
		Carqs = Carqs.filter(carinfo_id__year__in=query_anio)
	if((query_tipo)):
		Carqs = Carqs.filter(carinfo_id__type__in=query_tipo)
	if((query_combustible)):
		Carqs = Carqs.filter(carinfo_id__fuel__in=query_combustible)
	if((query_estatus)):
		Carqs = Carqs.filter(status__in=query_estatus)

	context = {
		'marcas': Marcas,
		'modelos': Modelos,
		'transmiciones': Transmiciones,
		'ciudades': Ciudad,
		'anios': Anios,
		'tipos': Tipos,
		'colores': Colores,
		'combustibles': Combustibles,
		'estatus': Estatus,
		'queryset': Carqs,
		'prueba': query_modelo
	}
	return render(request, "filtro.html", context)
	