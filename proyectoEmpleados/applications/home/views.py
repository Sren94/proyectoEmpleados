from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from .models import prueba
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
