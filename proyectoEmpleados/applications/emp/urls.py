from django.contrib import admin
from django.urls import path
from .views import listAllEmployees,listByArea,listBySearch
urlpatterns = [
    path('allEmployees/',listAllEmployees.as_view()),
    path('byArea/',listByArea.as_view()),
    path("search/",listBySearch.as_view())
]