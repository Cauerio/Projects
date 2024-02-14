from django.db import models

class Libro(models.Model):
    id_libro = models.AutoField(primary_key=True)
    nombre_libro = models.CharField(max_length=100)
    paginas = models.IntegerField() 