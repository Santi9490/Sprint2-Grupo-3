# manejador_de_pagos/models.py
from django.db import models
from cuenta.models import Cuenta

class Pago(models.Model):
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE, related_name="pagos")
    fecha_pago = models.DateTimeField(auto_now_add=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Pago de {self.monto} para {self.cuenta.estudiante.nombre} {self.cuenta.estudiante.apellido}"
