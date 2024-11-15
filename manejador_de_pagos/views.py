# manejador_de_pagos/views.py
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.urls import reverse
from gestor_usuario_roles.logic.estudiante_logic import get_estudiante_by_id
from gestor_usuario_roles.models import Estudiante
from .models import Pago
from .forms import CodigoEstudianteForm, PagoForm
from django.contrib.auth.decorators import login_required
from ofipensiones.auth0backend import getRole

@login_required
def pago_create(request):
    role = getRole(request)
    if role == "Rector" or role == "Coordinador":      
        if request.method == "POST":
            form = PagoForm(request.POST)
            if form.is_valid():
                cuenta = form.cleaned_data['cuenta']
                pago = form.save(commit=False)
                pago.save()
                cuenta.monto_pagado += pago.monto
                cuenta.saldo_pendiente = max(0, cuenta.saldo_pendiente - pago.monto)
                cuenta.pas_y_salvo = cuenta.saldo_pendiente == 0
                cuenta.save()
                messages.success(request, "Pago registrado exitosamente")
                return HttpResponseRedirect(reverse('pago_list'))
        else:
            print(form.errors)
    else:
        return HttpResponse("Unauthorized User")

@login_required
def pago_list(request, codigo=None):
    role = getRole(request)
    if role == "Rector" or role == "Coordinador" or role == "Secretaria":
        if codigo:
            estudiante = get_estudiante_by_id(codigo)
            pagos = Pago.objects.filter(cuenta__estudiante=estudiante)
        else:
            
            pagos = Pago.objects.all()

        context = {
            'pagos': pagos,
            'estudiante': estudiante if codigo else None
        }
        return render(request, 'manejador_de_pagos/pago_list.html', context)
        
    else:
        return HttpResponse("Unauthorized User")
    