from django.shortcuts import render

# Create your views here.
from .models import Doctor
from .models import Paciente

#Instanciamos las vistas genéricas de Django

from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

#Nos sirve para redireccionar despues de una acción revertiendo patrones de expresiones regulares

from django.urls import reverse
#Habilitamos el uso de mensajes en Django

from django.contrib import messages
#Habilitamos los mensajes para class-based views

from django.contrib.messages.views import SuccessMessageMixin
#Habilitamos los formularios en Django

from django import forms

class DoctorListado(ListView):
    model = Doctor # Llamamos a la clase 'Arepa' que se encuentra en nuestro archivo 'models.py' 
    
class PacienteListado(ListView):
    model = Paciente # Llamamos a la clase 'Arepa' que se encuentra en nuestro archivo 'models.py' 
    
class DoctorCrear(SuccessMessageMixin, CreateView): 
    model = Doctor # Llamamos a la clase 'Arepa' que se encuentra en nuestro archivo 'models.py'
    form = Doctor # Definimos nuestro formulario con el nombre de la clase o modelo 'Arepa'
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'arepas' de nuestra Base de Datos 
    success_message = 'Doctor Creada Correctamente!' # Mostramos este Mensaje luego de Crear una Arepa

    # Redireccionamos a la página principal luego de crear un registro o arepa
    def get_success_url(self):        
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
    

class PacienteCrear(SuccessMessageMixin, CreateView): 
    model = Paciente # Llamamos a la clase 'Arepa' que se encuentra en nuestro archivo 'models.py'
    form = Paciente # Definimos nuestro formulario con el nombre de la clase o modelo 'Arepa'
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'arepas' de nuestra Base de Datos 
    success_message = 'Paciente Creada Correctamente!' # Mostramos este Mensaje luego de Crear una Arepa

    # Redireccionamos a la página principal luego de crear un registro o arepa
    def get_success_url(self):        
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
    
    
class DoctorDetalle(DetailView): 
    model = Doctor # Llamamos a la clase 'Arepa' que se encuentra en nuestro archivo 'models.py' 
    
class PacienteDetalle(DetailView): 
    model = Paciente # Llamamos a la clase 'Arepa' que se encuentra en nuestro archivo 'models.py' 
    
    
class DoctorActualizar(SuccessMessageMixin, UpdateView): 
    model = Doctor # Llamamos a la clase 'Arepa' que se encuentra en nuestro archivo 'models.py' 
    form = Doctor # Definimos nuestro formulario con el nombre de la clase o modelo 'Arepa' 
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'arepas' de nuestra Base de Datos 
    success_message = 'Doctor Actualizada Correctamente !' # Mostramos este Mensaje luego de Editar un Arepa 

    # Redireccionamos a la página principal luego de actualizar un registro o arepa
    def get_success_url(self):               
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
    
class PacienteActualizar(SuccessMessageMixin, UpdateView): 
    model = Paciente # Llamamos a la clase 'Arepa' que se encuentra en nuestro archivo 'models.py' 
    form = Paciente # Definimos nuestro formulario con el nombre de la clase o modelo 'Arepa' 
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'arepas' de nuestra Base de Datos 
    success_message = 'Paciente Actualizada Correctamente !' # Mostramos este Mensaje luego de Editar un Arepa 

    # Redireccionamos a la página principal luego de actualizar un registro o arepa
    def get_success_url(self):               
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
    
    
class ArepaEliminar(SuccessMessageMixin, DeleteView): 
    model = Doctor 
    form = Doctor
    fields = "__all__"     

    # Redireccionamos a la página principal luego de eliminar un registro o arepa
    def get_success_url(self): 
        success_message = 'Doctor Eliminada Correctamente !' # Mostramos este Mensaje luego de Editar una Arepa 
        messages.success (self.request, (success_message))       
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
    
class ArepaEliminar(SuccessMessageMixin, DeleteView): 
    model = Paciente 
    form = Paciente
    fields = "__all__"     

    # Redireccionamos a la página principal luego de eliminar un registro o arepa
    def get_success_url(self): 
        success_message = 'Paciente Eliminada Correctamente !' # Mostramos este Mensaje luego de Editar una Arepa 
        messages.success (self.request, (success_message))       
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
    
    
