from django import forms
from .models import Colegio

class ColegioForm(forms.ModelForm):
    class Meta:
        model = Colegio
        fields = [
            'nombre',
            'direccion',
            'telefono',
            'email',
            'director',
        ]
        labels = {
            'nombre': 'Nombre del Colegio',
            'direccion': 'Dirección',
            'telefono': 'Teléfono',
            'email': 'Correo Electrónico',
            'director': 'Director del Colegio',
        }
