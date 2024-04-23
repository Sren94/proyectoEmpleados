from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import (ListView,DetailView,CreateView,TemplateView,UpdateView,DeleteView)
from .forms import newDepartamentoForm
# importamos los modelos 
from applications.emp.models import employee
from applications.dep.models import dep
from django.urls import reverse_lazy
from . import views
# Create your views here.

class newDepView(FormView):
    template_name='dep/registerDep.html'
    form_class= newDepartamentoForm
    success_url= reverse_lazy('dep_app:listDep')
    def form_valid(self, form):
        print('----------------------------estamos en el metodo---------------------')
        #se declara un objeto de departamento 
        #se debe respetar los nombres del modelo original 
        depa=views.dep(name= form.cleaned_data['dep'],shortName= form.cleaned_data['shortName'])
        #se salva en la base de datos la info       
        depa.save()
        #obtenemos datos con el formulario 
        firstName=form.cleaned_data['firstName']
        lastName=form.cleaned_data['lastName']
        email=form.cleaned_data['email']
        #creando el objeto y el registro de employee
        employee.objects.create(
            firstName=firstName,
            lastName=lastName,
            email=email,
            job='1',
            dep=depa
        )
        #se retorna al momento de sobreescribir (la vista,self)
        return super(newDepView,self).form_valid(form)

class depListView(ListView):
    context_object_name='dep'
    template_name = "dep/listDep.html"
    paginate_by=3
    ordering='id'
    def get_queryset(self):
        #print('++++++++++++++++++++++++++++')
        search = self.request.GET.get('search_dep','')
        print(f'{search}')
        list= dep.objects.filter(
            #aqui hace una busqueda al momento de enlazar la peticion
            name__icontains=search
            )
        #print(list)
        return list

class depDetailView(DetailView):
    model = dep
    template_name = "emp/listByArea.html"
    

