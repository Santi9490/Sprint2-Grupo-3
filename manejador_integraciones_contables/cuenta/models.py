from django.db import models
import requests

from cuenta.other import obtener_datos_estudiante
from ofipensiones import settings



class Cuenta(models.Model):
    estudiante = models.IntegerField(null=False, default=None)
    fecha_pago = models.DateField(null=True, blank=True)
    descripcion = models.CharField(max_length=255)
    pas_y_salvo = models.BooleanField(default=False)
    monto_pagado = models.DecimalField(max_digits=10, decimal_places=2)
    descuento = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    saldo_pendiente = models.DecimalField(max_digits=10, decimal_places=2)
    multa = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    fecha_vencimiento = models.DateField(null=True, blank=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        estudiante_detalle = obtener_datos_estudiante(self.estudiante)
        return f"Cuenta de {self.estudiante_detalle.nombre} {self.estudiante_detalle.apellido}"
    


