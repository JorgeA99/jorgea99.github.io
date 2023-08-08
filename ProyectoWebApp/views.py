from django.shortcuts import render, HttpResponse
from servicios.models import Servicios

# Create your views here.
def home(request):
    
    return render(request, "ProyectoWebApp/home.html")

def servicios(request):
    servicios=Servicios.objects.all()
    
    return render(request, "ProyectoWebApp/servicios.html", {"servicios":servicios})

def contratos(request):
    
    return render(request, "ProyectoWebApp/contratos.html")

def tienda(request):
    
   return render(request, "ProyectoWebApp/tienda.html")

def contacto(request):
    
    return render(request, "ProyectoWebApp/contacto.html")