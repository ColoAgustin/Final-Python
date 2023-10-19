from django.http import HttpResponse, HttpResponseServerError
from django.shortcuts import render, redirect
from AppAgustin.models import  Inicio, Noticias, Fechas, Pilotos, Aboutme
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from AppAgustin.forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from AppAgustin.forms import BuscaPilotosForm, PilotosFormulario
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from typing import List





# MIS VISTAS
def inicio(request):
    return render(request, 'index.html')

def noticias(request):
    return render(request, "noticias.html")
 
  
@login_required
def fechas(request):
    return render(request, "fechas.html")

def pilotos(request):
    
    registros = Pilotos.objects.all()
        
    return render(request, "pilotos.html", {'registros': registros} )

def aboutme(request):
    return render(request, "aboutme.html")
 


#FORMULARIO PARA LA BUSQUEDA DE PILOTOS

def form(request):
    if request.method == "POST":
        miFormulario = PilotosFormulario(request.POST) # info del html result
        # print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
           
            pilotos = Pilotos(nombre=informacion["nombre"], apellido=informacion["apellido"], imagen=informacion["imagen"])
            
            pilotos.save()
            
            return render(request, "index.html")
    
    else:
        miFormulario = PilotosFormulario()

    return render(request, "formulario.html", {"miFormulario": miFormulario})



#BUSQUEDA
def busqueda(request):
    if request.method == "POST":
        miFormulario = BuscaPilotosForm(request.POST) # info del html result

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            
            pilotos = Pilotos.objects.filter(nombre__icontains=informacion["pilotos"])

            return render(request, "resultados-busqueda.html", {"pilotos": pilotos})
    else:
        miFormulario = BuscaPilotosForm()

    return render(request, "busqueda.html", {"miFormulario": miFormulario})

#respuesta de la busqueda

def mostrar_pilotos(request):

    pilotos = Pilotos.objects.all() #trae todos los profesores

    contexto= {"pilotos":pilotos} 

    return render(request, "mostrarpilotos.html",contexto)

  

#login/logout registro mas logica


#login

def login_request(request):


      if request.method == "POST":
            form = AuthenticationForm(request, data = request.POST)

            if form.is_valid():
                  usuario = form.cleaned_data.get('username')
                  clave = form.cleaned_data.get('password')

                  nombre_usuario = authenticate(username=usuario, password=clave)

            
                  if nombre_usuario is not None:
                        login(request, nombre_usuario)
                       
                        return render(request,"index.html",  {"mensaje":f"Bienvenido {usuario}"} )
                  else:
                        form = AuthenticationForm()
                        return render(request,"login.html", {"mensaje":"Error, datos incorrectos", "form": form} )

            else:
                        
                        return render(request,"index.html" ,  {"mensaje":"Error, formulario erroneo"})

      form = AuthenticationForm()

      return render(request,"login.html", {'form':form} )


#logout
# def logout_request(request):
#       logout(request)
#       messages.info(request, "Saliste sin problemas")
#       return redirect("inicio")



#REGISTRO

def register(request):

      if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"index.html" ,  {"mensaje":"Usuario Creado :)"})


      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,"registro.html" ,  {"form":form})
    
    
#mixin para restringir una web del proyecto



#TEST DE BUSQUEDA NUMERO 2------------------------------------------------------------------------------------------

# def pilotos(request):
#     # Obtener la lista de pilotos de la base de datos
#     pilotos = Pilotos.objects.all()

#     # Obtener el nombre del piloto que el usuario desea buscar
#     piloto_buscado = request.GET.get("piloto")

#     # Iterar sobre la lista de pilotos
#     for piloto in pilotos:
#         # Si el nombre del piloto coincide con el que el usuario desea buscar
#         if piloto.nombre == piloto_buscado:
#             # Devolver el piloto encontrado
#             return render(request, "pilotos.html", {"piloto": piloto})

#     # Si el piloto no se encuentra, devolver un mensaje de error
#     return render(request, "pilotos.html", {"error": "El piloto no se encuentra"})
#








#CLASES PARA LOS ERRORES DE URL DEL USUARIO

class HomeView(TemplateView):
    template_name =  "index.html"
    
class VistaEjemplo(TemplateView):
    template_name = "ejemplo.html"
    
    def get_context_data(self, **kwargs):
        context = super(VistaEjemplo, self).get_context_data(**kwargs)
        a = 'prueba'
        print(a/10)
        return context
  
  

class Error404View(TemplateView):
    template_name = "error.html"
  


