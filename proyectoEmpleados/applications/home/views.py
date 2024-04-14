from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView
from .models import prueba
from django.urls import reverse_lazy
#importamos el modulo de forms tomando la clase pruebaForms
from .forms import pruebaForm
class indexView(TemplateView):
    template_name= 'home/home.html'
    
class pruebaListView(ListView):
    template_name ='home/prueba.html'
    queryset =['a','b','c']
    context_object_name='lista_prueba'
class texto(TemplateView):
    template_name='home/text.html'

class modeloListView(ListView):
    model = prueba
    template_name = "home/listPrueba.html"
    context_object_name =  'objeto'


class crearCreateView(CreateView):
    model = prueba
    template_name = "home/add.html"
    #usanso los formularios personalizados
    form_class=pruebaForm
    success_url = reverse_lazy('home_app:index')
   
    