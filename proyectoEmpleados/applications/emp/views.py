from django.shortcuts import render
from .models import employee
from django.views.generic import (ListView,DetailView,CreateView)
# Create your views here.
class listAllEmployees(ListView):
    model = employee
    context_object_name = 'employees'
    template_name='emp/listAllEmployees.html'
    paginate_by=5
    ordering='dep'
class listByArea(ListView):
    model = employee
    template_name='emp/listByarea.html'
    def get_queryset(self):
        var= self.kwargs['var']
        list =employee.objects.filter(dep__name=var)
        return list
    
    #employee.objects.filter(dep__name=var)
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
class skillsEmployee(ListView):
    model = employee
    template_name = "emp/listSkills.html"
    context_object_name = 'skills'
    def get_queryset(self):
        emp_id = self.request.GET.get('emp','')
        print(emp_id)
        if emp_id:
            try:
                emp = employee.objects.get(id=emp_id)
                return emp.skill.all()
            except employee.DoesNotExist:
                return ['No existe el id']
        else: return ['ingresa un valor ']

class employeeDetailView(DetailView):
    model = employee
    template_name = "emp/employeeDetail.html"
    def get_context_data(self, **kwargs) -> dict[str, any]:
        context = super(employeeDetailView,self).get_context_data(**kwargs)
        context["Titulo"] = 'empleado del mes'
        return context

class employeeCreateView(CreateView):
    model = employee
    template_name = "emp/registerEmployee.html"
    #fields = ['firstName','lastName','email']
    fields = ('__all__')


    
