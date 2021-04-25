from django.contrib import admin
from django.urls import path
from cars import views  as car_views
from delete import views  as delete_views
from update import views  as update_views
from users import views as users_views
from filter import views as filter_views
#from django.views.generic import TemplateView
from rest_framework_simplejwt.views import (
TokenObtainPairView,
TokenRefreshView,
)


urlpatterns = [
    path('', car_views.car_list),
    path('prueba/', car_views.prueba),
    path('admin/', admin.site.urls),
    path('cars/', car_views.indexpage ),
    path('cars/r',car_views.guardar),
    path('cars/lista_car', car_views.lista_car, name='lista_car'),
    path('delete/', delete_views.indexpage),
    path('delete/r',delete_views.eliminar),
    path('update/', update_views.indexpage),
    path('update/elegir',update_views.elegir),
    path('update/editar',update_views.editar),
    path('users/', users_views.index),
    path('users/create_user',users_views.agregar),
    path('cars/get',car_views.extraer_datos),
    path('filter/',filter_views.form),
]
