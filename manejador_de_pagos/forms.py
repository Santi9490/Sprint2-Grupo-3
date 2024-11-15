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
            'monto': 'Monto del pago',
            'descripcion': 'Descripción'
        }

    def __init__(self, *args, **kwargs):
        estudiante = kwargs.pop('estudiante', None)
        super(PagoForm, self).__init__(*args, **kwargs)
        if estudiante:
            # Filtra las cuentas solo para el estudiante especificado
            self.fields['cuenta'].queryset = Cuenta.objects.filter(estudiante=estudiante)

class CodigoEstudianteForm(forms.Form):
    codigo = forms.CharField(label="Código del Estudiante", max_length=20)