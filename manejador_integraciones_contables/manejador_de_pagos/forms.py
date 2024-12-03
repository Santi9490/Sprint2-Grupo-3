# manejador_de_pagos/forms.py
from django import forms
from .models import Pago
from cuenta.models import Cuenta

class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = ['estudiante', 'cuenta', 'monto', 'descripcion']
        labels = {
            'estudiante': 'Estudiante',
            'cuenta': 'Cuenta',
            'monto': 'Monto del pago',
            'descripcion': 'Descripción'
        }

    def __init__(self, *args, **kwargs):
        super(PagoForm, self).__init__(*args, **kwargs)
        # Solo muestra cuentas asociadas al estudiante seleccionado
        self.fields['cuenta'].queryset = Cuenta.objects.none()

        if 'estudiante' in self.data:
            try:
                estudiante_codigo = int(self.data.get('estudiante'))
                self.fields['cuenta'].queryset = Cuenta.objects.filter(estudiante_codigo=estudiante_codigo)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['cuenta'].queryset = Cuenta.objects.filter(estudiante=self.instance.estudiante)



