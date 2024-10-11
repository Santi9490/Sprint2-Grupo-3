from django.db import models

class Colegio(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=250)
    telefono = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre


