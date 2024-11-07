from django import forms
from .models import EstadoCuenta, Estudiante

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = [
            'nombre',
            'apellido',
            'codigo',
            'fecha_nacimiento',
            'numero_acudiente',
            'direccion',
        ]
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'codigo': 'Código',
            'fecha_nacimiento': 'Fecha de Nacimiento',
            'numero_acudiente': 'Número del Acudiente',
            'direccion': 'Dirección',
        }
class EstadoCuentaForm(forms.ModelForm):
    class Meta:
        model = EstadoCuenta
        fields = [
            'estudiante',
            'fecha_pago',
            'descripcion',
            'monto_pagado',
            'saldo_pendiente',
            'multa',
            'fecha_vencimiento',
        ]
        labels = {
            'estudiante': 'Estudiante',
            'fecha_pago': 'Fecha de Pago',
            'descripcion': 'Descripción',
            'monto_pagado': 'Monto Pagado',
            'saldo_pendiente': 'Saldo Pendiente',
            'multa': 'Multa',
            'fecha_vencimiento': 'Fecha de Vencimiento',
        }