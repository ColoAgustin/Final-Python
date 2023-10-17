from django.http import HttpResponse
from django.shortcuts import render
from AppAgustin.models import  Inicio, Noticias, Fechas, Pilotos, Aboutme
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from AppAgustin.forms import UserRegisterForm
from django.contrib.auth.decorators import login_required




# MIS VISTAS
def inicio(request):
    return render(request, 'index.html')

def noticias(request):
    return render(request, "noticias.html")
  
@login_required
def fechas(request):
    return render(request, "fechas.html")

def pilotos(request):
    return render(request, "pilotos.html")

def aboutme(request):
    return render(request, "aboutme.html")
 


#FORMULARIO PARA LA BUSQUEDA DE PILOTOS

# def pilotos(request):
#   pilotos = Pilotos.objects.all()

#   if request.method == "POST":
#     nombre = request.POST["nombre"]
#     pilotos = pilotos.filter(nombre__icontains=nombre)

#   return render(request, "pilotos.html", {
#     "pilotos": pilotos,
#   })
  
  

#login/logout registro mas logica

#login

def login_request(request):


      if request.method == "POST":
            form = AuthenticationForm(request, data = request.POST)

            if form.is_valid():
                  usuario = form.cleaned_data.get('username')
                  contrasena = form.cleaned_data.get('password')

                  nombre_usuario = authenticate(username=usuario, password=contrasena)

            
                  if nombre_usuario is not None:
                        login(request, nombre_usuario)
                       
                        return render(request,"index.html",  {"mensaje":f"Bienvenido {usuario}"} )
                  else:
                        
                        return render(request,"index.html", {"mensaje":"Error, datos incorrectos"} )

            else:
                        
                        return render(request,"index.html" ,  {"mensaje":"Error, formulario erroneo"})

      form = AuthenticationForm()

      return render(request,"login.html", {'form':form} )




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





  
  

  


