# manejador_de_pagos/models.py
from django.db import models
from cuenta.models import Cuenta

class Pago(models.Model):
    estudiante = models.IntegerField(null=False, default=None)
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE, default=None)
    fecha_pago = models.DateTimeField(auto_now_add=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Pago de {self.monto} para estudiante con ID {self.estudiante}"
