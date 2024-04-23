from django.contrib import admin
from django.urls import path
from . import views
app_name='dep_app'
urlpatterns = [
    path(
        "registerDep/",
        views.newDepView.as_view(),
        name="registerDep"
    ),
    path(
        "listDep/",
        views.depListView.as_view(),
        name="listDep"
    )
]