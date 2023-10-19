from django import forms
from AppAgustin.models import Pilotos
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User



#BUSQUEDA Y FORMULARIO DE PILOTOS

class PilotosFormulario(forms.Form):
    nombre  = forms.CharField()
    apellido = forms.CharField()
    imagen = forms.CharField()
    
#BUSQUEDA
class BuscaPilotosForm(forms.Form):
    pilotos = forms.CharField()




#USER REGISTER
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
 
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # Sacar los mensajes de ayuda
        help_texts = {k:"" for k in fields}
        
        
        
        




