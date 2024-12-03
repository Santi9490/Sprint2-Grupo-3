# manejador_de_pagos/views.py
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.urls import reverse
import requests
from cuenta.models import Cuenta
from manejador_estudiantes.ofipensiones import settings
from .models import Pago
from .forms import PagoForm
from django.contrib.auth.decorators import login_required
from ofipensiones.auth0backend import getRole

def get_estudiante(data):
    r = requests.get(settings.PATH_ESTUDIANTES, headers={"Accept":"application/json"})
    estudiantes = r.json()
    for estudiante in estudiantes:
        if data["estudiante"] == estudiante["codigo"]:
            return estudiante["codigo"]
    return -1


def pago_create(request):
    role = getRole(request)
    if role == "Rector" or role == "Coordinador":
        if request.method == "POST":
            form = PagoForm(request.POST)
            if form.is_valid():
                pago = form.save(commit=False)
                cuenta = form.cleaned_data['cuenta']
                pago.save()

                # Actualiza la cuenta
                cuenta.monto_pagado += pago.monto
                cuenta.saldo_pendiente = max(0, cuenta.saldo_pendiente - pago.monto)
                cuenta.pas_y_salvo = cuenta.saldo_pendiente == 0
                cuenta.save()

                messages.success(request, "Pago registrado exitosamente")
                return redirect(reverse('pago_list'))
        else:
            form = PagoForm()

        return render(request, 'manejador_de_pagos/pago_create.html', {'form': form})
    else:
        return HttpResponse("Unauthorized User")



@login_required
def pago_list(request, id=None):
    role = getRole(request)
    if role in ["Rector", "Coordinador", "Secretaria"]:
        if id:
            pagos = Pago.objects.filter(id=id)
        else:
            pagos = Pago.objects.all()

        return render(request, 'manejador_de_pagos/pago_list.html', {'pagos': pagos})
    else:
        return HttpResponse("Unauthorized User")

@login_required
def pago_list(request):
    role = getRole(request)
    if role in ["Rector", "Coordinador", "Secretaria"]:
        if id:
            pagos = Pago.objects.filter(id=id)
        else:
            pagos = Pago.objects.all()

        return render(request, 'manejador_de_pagos/pago_list.html', {'pagos': pagos})
    else:
        return HttpResponse("Unauthorized User")

    
@login_required
def obtener_cuentas_por_estudiante(request, estudiante_id):
    cuentas = Cuenta.objects.filter(estudiante_id=estudiante_id)
    data = [{'id': cuenta.id, 'descripcion': cuenta.descripcion} for cuenta in cuentas]
    return JsonResponse(data, safe=False)

def generar_reporte(request, estudiante_id):
    cuentas = Cuenta.objects.filter(estudiante_id=estudiante_id)
    data = [{'id': cuenta.id, 'descripcion': cuenta.descripcion} for cuenta in cuentas]
    # TODO: Generar un descargable con todas las cuentas y pagos del estudiante
    return JsonResponse(data, safe=False)


