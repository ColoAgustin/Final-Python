from django.contrib import admin
from .models import  Inicio, Noticias, Fechas, Pilotos, Aboutme

# Register your models here.
admin.site.register(Inicio)
admin.site.register(Noticias)
admin.site.register(Fechas)
admin.site.register(Pilotos)
# admin.site.register(Login)
admin.site.register(Aboutme)

