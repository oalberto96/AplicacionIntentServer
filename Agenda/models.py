from django.db import models

# Create your models here.
class Contacto(models.Model):
    nombre = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
