from django.contrib import admin
from django.urls import path
from .views import listAllEmployees,listByArea,listBySearch,skillsEmployee,employeeDetailView,employeeCreateView
urlpatterns = [
    path('allEmployees/',listAllEmployees.as_view()),
    path('byArea/<var>/',listByArea.as_view()),
    path("search/",listBySearch.as_view()),
    path('skills/',skillsEmployee.as_view()),
    path('detail/<pk>', employeeDetailView.as_view()),
    path('register/', employeeCreateView.as_view()),
]