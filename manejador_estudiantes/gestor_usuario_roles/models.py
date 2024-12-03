from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    codigo = models.CharField(max_length=20, default='0000')  
    fecha_nacimiento = models.DateField(null=True, blank=True)
    numero_acudiente = models.CharField(max_length=15, default='0000000000')
    direccion = models.CharField(max_length=100, default='Sin Dirección')  

    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellido)


