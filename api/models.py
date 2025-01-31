from django.db import models

# Create your models here.

class DatosProgramadores(models.Model):
    NombreCompleto = models.CharField(max_length=100)
    Apodo = models.CharField(max_length=50)
    Edad = models.PositiveSmallIntegerField()
    Estado = models.CharField(max_length=1)