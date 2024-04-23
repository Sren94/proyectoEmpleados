from django.contrib import admin
from django.urls import path
from . import views
app_name ='emp_app'
urlpatterns = [
    #path
    # (
         #nombreParaLaURL#,
         #vista.as_view(),
         #nombre='nombreDeLaVista'    
    #)
    path(
        "",
        views.indexTemplate.as_view(),
        name="index"
    ),
    
    path(
        'allEmployees/',
         views.listAllEmployeesListView.as_view(),
        name='allEmployees'),
    
    path('byArea/<var>/',
         views.listByAreaListView.as_view(),
         name='byArea'),
    
    path("search/",
         views.listBySearchListView.as_view(),
         name='search'),
    
    path('skills/',
         views.skillsEmployeeListView.as_view(),
         name='skills'),
    
    path('detail/<pk>',
         views.employeeDetailView.as_view(),
         name='detail'),
    
    path('register/',
         views.employeeCreateView.as_view(),
         name='register'),
    
    path('success/',
         views.successView.as_view(),
         name='success'),
    path(
         'update/<pk>',
          views.employeeUpdateView.as_view(),
          name='update'
    ),
    path(
     'delete/<pk>',
     views.employeeDeleteView.as_view(),
     name='delete'
    ),
]