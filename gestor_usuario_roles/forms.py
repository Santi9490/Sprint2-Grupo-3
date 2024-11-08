from django import forms
from .models import Estudiante

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