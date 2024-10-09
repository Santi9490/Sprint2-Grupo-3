from django import forms
from .models import Estudiante

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = [
            'nombre',
            'apellido',
            'codigo',
            'numero_acudiente',
            'fecha_nacimiento',
            'direccion',
        ]
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'codigo': 'Código',
            'numero_acudiente': 'Número del Acudiente',
            'fecha_nacimiento': 'Fecha de Nacimiento',
            'direccion': 'Dirección',
        }
