from django.db import models

from gestor_usuario_roles.models import Estudiante

class Cuenta(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, default=None)
    codigo = models.ForeignKey(Estudiante.codigo, on_delete=models.CASCADE, default=None)
    fecha_pago = models.DateField(null=True, blank=True)
    descripcion = models.CharField(max_length=255)
    pas_y_salvo = models.BooleanField(default=False)
    monto_pagado = models.DecimalField(max_digits=10, decimal_places=2)
    saldo_pendiente = models.DecimalField(max_digits=10, decimal_places=2)
    multa = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    fecha_vencimiento = models.DateField(null=True, blank=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cuenta de {self.estudiante.nombre} {self.estudiante.apellido}"
