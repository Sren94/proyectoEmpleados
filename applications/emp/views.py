from .models import employee
from django.views.generic import (ListView,DetailView,CreateView,TemplateView,UpdateView,DeleteView)
from django.urls import reverse_lazy
# Create your views here.

#la listView sirve para mostrar datos
class listAllEmployeesListView(ListView):
    model = employee
    context_object_name = 'employees'
    template_name='emp/listAllEmployees.html'
    paginate_by=5
    ordering='id'
class listByAreaListView(ListView):
    model = employee
    template_name='emp/listByarea.html'
    def get_queryset(self):
        var= self.kwargs['var']
        list =employee.objects.filter(dep__name=var)
        return list
    
    #employee.objects.filter(dep__name=var)
    context_object_name = 'employees'
class listBySearchListView(ListView):
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
class skillsEmployeeListView(ListView):
    model = employee
    template_name = "emp/listSkills.html"
    context_object_name = 'skills'
    #sobreescritura de la lista de un objeto
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

#el DetailView sirve para dar detalles especificos de un dato
class employeeDetailView(DetailView):
    model = employee
    template_name = "emp/employeeDetail.html"
    def get_context_data(self, **kwargs) -> dict[str, any]:
        #manda una variable adicional al html
        context = super(employeeDetailView,self).get_context_data(**kwargs)
        context["Titulo"] = 'empleado del mes'
        return context

class successView(TemplateView):
    template_name = "emp/success.html"

class employeeCreateView(CreateView):
    model = employee
    template_name = "emp/registerEmployee.html"
    fields = [
        'firstName',
        'lastName',
        'email',
        'job',
        'dep',
        'skill']
    #cuando el forms esta validado se sobreescribre el proceso
    def form_valid(self, form):
        #logica del proceso
        employee=form.save()
        employee.fullName=employee.firstName+' '+employee.lastName
        employee.save()
        #se sobreescribe el metodo de la clase donde estamos trabajando
        #asi como se retorna los cambios
        return super(employeeCreateView,self).form_valid(form)
    
    #este parametro es obligatorio para que el create view 
    #fields = ('__all__')
    #se toma los parametros del archivo urls.py
    #se redirecciona de la sig forma app_name:nombreDeLaVista 
    success_url= reverse_lazy('emp_app:success')

class employeeUpdateView(UpdateView):
    model = employee
    template_name = "emp/updateEmployee.html"
    fields=['dep','job','email']
    success_url =reverse_lazy('emp_app:success')
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        #tambien sera el manejo de procesos en este metodo
        #request = maneja todo lo relacionado a los metodos http y asi
        #obtener sus propiedades y lo maneja de manera de diccionario 
        
        print(request.POST)
        #aqui se es el manejo de atributos 
        print(request.POST['email'])
        
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        print('Metodo Self')
        return super().form_valid(form)
    
class employeeDeleteView(DeleteView):
    model = employee
    template_name = "emp/deleteEmployee.html"
    success_url =reverse_lazy('emp_app:success')



