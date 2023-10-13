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
    
class Aboutme(models.Model):
    sobremi = models.CharField(max_length=40)
