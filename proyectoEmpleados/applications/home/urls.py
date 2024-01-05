from django.urls import path,include
from . import views
urlpatterns = [
    path('home/',views.indexView.as_view()),
    path('prueba/',views.pruebaListView.as_view()),
    path('text/',views.texto.as_view()),
    path('lista/',views.modeloListView.as_view())
]
