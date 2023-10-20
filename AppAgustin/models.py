from django.db import models

# MIS MODELS

class Inicio(models.Model):
    inicio = models.CharField(max_length=40)
    
class Noticias(models.Model):
    noticias = models.CharField(max_length=40)

class Fechas(models.Model):
    fechas = models.CharField(max_length=40)
    
class Pilotos(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    imagen = models.CharField(max_length=300, default="https://media.formula1.com/d_driver_fallback_image.png/content/dam/fom-website/drivers/M/MAXVER01_Max_Verstappen/maxver01.png.transform/2col/image.png")
    imagen_bandera = models.CharField(max_length=300, default="https://media.formula1.com/content/dam/fom-website/flags/Netherlands.gif")
class Aboutme(models.Model):
    sobremi = models.CharField(max_length=40)
