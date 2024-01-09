from django.shortcuts import render
from .models import employee
from django.views.generic import (ListView)
# Create your views here.
class listAllEmployees(ListView):
    model = employee
    context_object_name = 'employees'
    template_name='emp/listAllEmployees.html'
class listByArea(ListView):
   # model = employee
    
    template_name='emp/listByarea.html'
    queryset=employee.objects.filter(dep__name='Contaduria')
    context_object_name = 'employees'