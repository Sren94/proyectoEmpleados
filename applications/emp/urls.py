from django.contrib import admin
from django.urls import path
from .views import listAllEmployeesListView,listByAreaListView,listBySearchListView,skillsEmployeeListView,employeeDetailView,employeeCreateView,successView,employeeUpdateView,employeeDeleteView
app_name ='emp_app'
urlpatterns = [
    #path
    # (
         #nombreParaLaURL#,
         #vista.as_view(),
         #nombre='nombreDeLaVista'    
    #)
    path(
        'allEmployees/',
        listAllEmployeesListView.as_view(),
        name='allEmployees'),
    
    path('byArea/<var>/',
         listByAreaListView.as_view(),
         name='byArea'),
    
    path("search/"
         ,listBySearchListView.as_view(),
         name='search'),
    
    path('skills/',
         skillsEmployeeListView.as_view(),
         name='skills'),
    
    path('detail/<pk>',
         employeeDetailView.as_view(),
         name='detail'),
    
    path('register/',
         employeeCreateView.as_view(),
         name='register'),
    
    path('success/',
         successView.as_view(),
         name='success'),
    path(
     'update/<pk>',
     employeeUpdateView.as_view(),
     name='update'
    ),
    path(
     'delete/<pk>',
     employeeDeleteView.as_view(),
     name='detele'
    ),
]