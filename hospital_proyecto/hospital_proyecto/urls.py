"""
URL configuration for hospital_proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path 
from  hospital_app.views import DoctorListado, DoctorDetalle, DoctorCrear, DoctorActualizar, DoctorEliminar
from  hospital_app.views import PacienteListado, PacienteDetalle, PacienteCrear, PacienteActualizar, PacienteEliminar

urlpatterns = [

    path('admin/', admin.site.urls),

    # La ruta 'leer' en donde listamos todos los registros o arepas de la Base de Datos
    path('doctores/', DoctorListado.as_view(template_name = "adoctores/index.html"), name='leer'),
    path('pacientes/', PacienteListado.as_view(template_name = "pacientes/index.html"), name='leer'),

    # La ruta 'detalles' en donde mostraremos una página con los detalles de un arepas o registro 
    path('doctores/detalle/<int:pk>', DoctorDetalle.as_view(template_name = "doctores/detalles.html"), name='detalles'),*
    path('pacientes/detalle/<int:pk>', PacienteDetalle.as_view(template_name = "pacientes/detalles.html"), name='detalles'),

    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo arepas o registro  
    path('doctores/crear', DoctorCrear.as_view(template_name = "doctores/crear.html"), name='crear'),
    path('pacientes/crear', PacienteCrear.as_view(template_name = "pacientes/crear.html"), name='crear'),

    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un arepas o registro de la Base de Datos 
    path('doctores/editar/<int:pk>', DoctorActualizar.as_view(template_name = "doctores/actualizar.html"), name='actualizar'),
    path('pacientes/editar/<int:pk>', PacienteActualizar.as_view(template_name = "pacientes/actualizar.html"), name='actualizar'), 

    # La ruta 'eliminar' que usaremos para eliminar un arepas o registro de la Base de Datos 
    path('doctores/eliminar/<int:pk>', DoctorEliminar.as_view(), name='eliminar'), 
    path('pacientes/eliminar/<int:pk>', PacienteEliminar.as_view(), name='eliminar'),  
]