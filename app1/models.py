from django.db import models

# Create your models


class MascotaM(models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.CharField(max_length=2)
    tipo = models.CharField(max_length=40)
    raza = models.CharField(max_length=40)
    