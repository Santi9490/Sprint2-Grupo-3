from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
import requests

from cuenta.models import Cuenta
from cuenta.forms import CuentaForm
from manejador_estudiantes.ofipensiones import settings

def cuenta_list(request):
    estados_cuenta = Cuenta.objects.select_related('estudiante').all()
    context = {
        'cuenta_list': estados_cuenta
    }
    return render(request, 'cuenta/cuentas.html', context)

# Función para crear un nuevo estado de cuenta
def cuenta_create(request):
    if request.method == 'POST':
        form = CuentaForm(request.POST)
        if form.is_valid():
            form.save() 
            messages.add_message(request, messages.SUCCESS, 'Estado de cuenta creado exitosamente')
            return HttpResponseRedirect(reverse('cuenta_create'))
        else:
            print(form.errors)
    else:
        form = CuentaForm()

    context = {
        'form': form,
    }
    return render(request, 'cuenta/cuentaCreate.html', context)

# Función para ver el estado de cuenta de un solo estudiante con todos sus registros
def cuenta_detalle(request):
    estudiante = get_estudiante(request)
    if estudiante == -1:
        return JsonResponse({"error": "Estudiante no encontrado"}, status=404)
    else:
        estados_cuenta = Cuenta.objects.filter(estudiante=estudiante)
        context = {
            'estudiante': estudiante,
            'estados_cuenta': estados_cuenta
        }
        return render(request, 'cuenta/cuenta_detalle.html', context)


def get_estudiante(data):
    r = requests.get(settings.PATH_ESTUDIANTES, headers={"Accept":"application/json"})
    estudiantes = r.json()
    for estudiante in estudiantes:
        if data["estudiante"] == estudiante["codigo"]:
            return estudiante["codigo"]
    return -1
