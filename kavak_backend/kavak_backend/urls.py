from django.contrib import admin
from django.urls import path
from cars import views  as car_views
from delete import views  as delete_views
from update import views  as update_views
#from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('hola-mundo/', car_views.hola_mundo, name="hola_mundo")
    #TemplateView.as_view(template_name = "index.html")
    
    path('cars/', car_views.indexpage ),
    path('cars/r',car_views.guardar),
    path('cars/lista_car', car_views.lista_car, name='lista_car'),
    path('delete/', delete_views.indexpage),
    path('delete/r',delete_views.eliminar),
    path('update/', update_views.indexpage),
    path('update/elegir',update_views.elegir),
    path('update/editar',update_views.editar)

]
