from django import forms
from .models import Cuenta

class CuentaForm(forms.ModelForm):
    class Meta:
        model = Cuenta
        fields = [
            'estudiante',
            'codigo',
            'fecha_pago',
            'descripcion',
            'pas_y_salvo',
            'monto_pagado',
            'saldo_pendiente',
            'multa',
            'fecha_vencimiento',
        ]
        labels = {
            'estudiante': 'Estudiante',
            'codigo': 'Código',
            'fecha_pago': 'Fecha de Pago',
            'descripcion': 'Descripción',
            'pas_y_salvo': 'Pas y Salvo',
            'monto_pagado': 'Monto Pagado',
            'saldo_pendiente': 'Saldo Pendiente',
            'multa': 'Multa',
            'fecha_vencimiento': 'Fecha de Vencimiento',
        }