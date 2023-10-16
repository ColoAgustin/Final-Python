from django.http import HttpResponse
from django.shortcuts import render
from AppAgustin.models import Inicio, Noticias, Fechas, Pilotos, Aboutme


# MIS VISTAS
def inicio(request):
    return render(request, 'index.html')

def noticias(request):
    return render(request, "noticias.html")

def fechas(request):
    return render(request, "fechas.html")

def pilotos(request):
    return render(request, "pilotos.html")

def aboutme(request):
    return render(request, "aboutme.html")


#FORMULARIO PARA LA BUSQUEDA DE PILOTOS

def pilotos(request):
  pilotos = Pilotos.objects.all()

  if request.method == "POST":
    nombre = request.POST["nombre"]
    pilotos = pilotos.filter(nombre__icontains=nombre)

  return render(request, "pilotos.html", {
    "pilotos": pilotos,
  })
