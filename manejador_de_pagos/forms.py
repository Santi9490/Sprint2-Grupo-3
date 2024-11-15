# manejador_de_pagos/forms.py
from django import forms
from .models import Pago
from cuenta.models import Cuenta
from gestor_usuario_roles.models import Estudiante

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
                estudiante_id = int(self.data.get('estudiante'))
                self.fields['cuenta'].queryset = Cuenta.objects.filter(estudiante_id=estudiante_id)
            except (ValueError, TypeError):
                pass  # Mantener queryset vacío si no es válido
        elif self.instance.pk:
            self.fields['cuenta'].queryset = Cuenta.objects.filter(estudiante=self.instance.estudiante)



