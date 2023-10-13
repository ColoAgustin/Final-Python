from django.shortcuts import render
from AppAgustin.models import Inicio, Noticias, Fechas, Pilotos, Aboutme


# MIS VISTAS
def inicio(request):
    return render(request, 'index.html')

def noticias(request):
    return render(request, "AppAgustin/noticias.html")

def fechas(request):
    return render(request, "AppAgustin/fechas.html")

def pilotos(request):
    return render(request, "AppAgustin/pilotos.html")

def aboutme(request):
    return render(request, "AppAgustin/aboutme.html")