# Backend_O.o
Aquí se anexara todo lo necesario para el desarrollo del Backend del proyecto de Ingeniería en Software.

### Indicaciones para nuevos developers

Para la ejecución del backend en la máquina local se debe clonar el repositorio
, principalmente la carpeta kavak_backend. Para su ejecución es necesario tener instalado django, django
rest y json web token. Ejemplo en terminal de windows:

- python -m pip install Django

- pip install djangorestframework

- pip install djangorestframework-simplejwt

- python -m pip install django-cors-headers

- pip install markdown       # Markdown support for the browsable API.

- pip install django-filter  # Filtering support

Una vez teniendo instalado todo lo necesario unicamente tiene que ejecutarse 
la carpeta de proyecto con el comando en terminal "python manage.py runserver". 
Una vez ejecutado el proyecto puede accederse a las direcciones:

- cars/ : se visualiza un formulario html de prueba para los endpoints.

- cars/r: al enviar los datos ingresados en el formulario de prueba.

- cars/lista_car: al escribir 0 en formulario de prueba despliega la lista de carros en la base de datos.

- delete/: formulario html de prueba para colocar el coche a eliminar.

- delete/r: al enviar el coche a eliminar.

- update/: formulario prueba para modificar campo seleccionado.

- update/elegir: campo seleccionado.

- update/editar: al enviar el campo modificado.

- users/: formulario de prueba para ingresar usuario.

- users/create_user: enviar el usuario ingresado.

