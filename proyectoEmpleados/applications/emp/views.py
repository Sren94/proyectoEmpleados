from django.shortcuts import render
from .models import employee
from django.views.generic import (ListView)
# Create your views here.
class listAllEmployees(ListView):
    model = employee
    context_object_name = 'employees'
    template_name='emp/listAllEmployees.html'
    paginate_by=5
    ordering='dep'
class listByArea(ListView):
   # model = employee
    
    template_name='emp/listByarea.html'
    queryset=employee.objects.filter(dep__name='Contaduria')
    context_object_name = 'employees'
class listBySearch(ListView):
    model = employee
    template_name = "emp/search.html"
    context_object_name='employees'
    def get_queryset(self):
        print('++++++++++++++++++++++++++++')
        search = self.request.GET.get('search','')
        print(f'{search}')
        list= employee.objects.filter(firstName=search)
        print(list)
        return list
        
    
