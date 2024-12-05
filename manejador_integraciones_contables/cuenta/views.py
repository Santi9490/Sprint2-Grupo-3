from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
import requests

from cuenta.models import Cuenta
from cuenta.forms import CuentaForm
from ofipensiones import settings
from other import obtener_datos_estudiante

def cuenta_list(request):
    cuentas = Cuenta.objects.all()
    cuentas_con_datos = []
    for cuenta in cuentas:
        estudiante_datos = obtener_datos_estudiante(cuenta.estudiante)
        cuentas_con_datos.append({
            'cuenta': cuenta,
            'estudiante': estudiante_datos
        })
    return render(request, 'cuenta/cuentas.html', {'cuenta_list': cuentas_con_datos})


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
    try:
        response = requests.get(settings.PATH_ESTUDIANTES, headers={"Accept": "application/json"})
        if response.status_code == 200:
            estudiantes = response.json()
            for estudiante in estudiantes:
                if str(data["estudiante"]) == str(estudiante["codigo"]):  # Asegúrate de que ambos sean cadenas
                    return estudiante
    except requests.RequestException as e:
        print(f"Error al obtener lista de estudiantes: {e}")
    return None

