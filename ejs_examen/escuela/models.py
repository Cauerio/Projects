from django.db import models


class Alumno(models.Model):
    DNI = models.CharField(max_length=9, unique=True, primary_key=True)
    nombre = models.CharField(max_length=20)

 

