from django.urls import path
from ProyectoWebApp import views



urlpatterns = [
    path('', views.home, name="home"),
    path('servicios', views.servicios, name="servicios"),
    path('contratos', views.contratos, name="contratos"),
    path('tienda', views.tienda, name="tienda"),
    path('contacto', views.contacto, name="contacto"),
]
