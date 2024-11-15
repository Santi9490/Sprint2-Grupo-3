# manejador_de_pagos/forms.py
from django import forms
from .models import Pago
from cuenta.models import Cuenta

class PagoForm(forms.ModelForm):

    class Meta:
        model = Pago
        fields = ['estudiante','cuenta', 'monto', 'descripcion']
        labels = {
            'estudiante': 'Estudiante',
            'cuenta': 'Cuenta',
            'monto': 'Monto del pago',
            'descripcion': 'Descripción'
        }

