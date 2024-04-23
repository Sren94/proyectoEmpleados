from django.urls import path,include
from . import views
app_name ='home_app'
urlpatterns = [
    path('prueba/',views.pruebaListView.as_view()),
    path('text/',views.texto.as_view()),
    path('lista/',views.modeloListView.as_view()),
    path('add/',views.crearCreateView.as_view()),
    path('css/',views.pruebaCssView.as_view(),name='css'),
]
