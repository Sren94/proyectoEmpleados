from django.contrib import admin
from django.urls import path
from .views import listAllEmployees,listByArea,listBySearch,skillsEmployee,employeeDetailView,employeeCreateView,successView
app_name ='emp_app'
urlpatterns = [
    path(
        'allEmployees/',
        listAllEmployees.as_view(),
        name='allEmployees'),
    
    path('byArea/<var>/',
         listByArea.as_view(),
         name='byArea'),
    
    path("search/"
         ,listBySearch.as_view(),
         name='search'),
    
    path('skills/',
         skillsEmployee.as_view(),
         name='skills'),
    
    path('detail/<pk>',
         employeeDetailView.as_view(),
         name='detail'),
    
    path('register/',
         employeeCreateView.as_view(),
         name='register'),
    
    path('success/',
         successView.as_view(),
         name='success')
]