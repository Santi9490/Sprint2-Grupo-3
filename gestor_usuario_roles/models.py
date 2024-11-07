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
    
class EstadoCuenta(models.Model):
    estudiante = models.ForeignKey('Estudiante', on_delete=models.CASCADE, related_name='estados_cuenta')
    fecha_pago = models.DateField(null=True, blank=True)
    descripcion = models.CharField(max_length=255)
    monto_pagado = models.DecimalField(max_digits=10, decimal_places=2)
    saldo_pendiente = models.DecimalField(max_digits=10, decimal_places=2)
    multa = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    fecha_vencimiento = models.DateField(null=True, blank=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Estado de cuenta de {self.estudiante.nombre} {self.estudiante.apellido}"


