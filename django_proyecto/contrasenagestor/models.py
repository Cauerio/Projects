# Create your models here.

from django.db import models

class Datos(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=50)
    password = models.CharField(max_length=50)



    

