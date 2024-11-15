# manejador_de_pagos/views.py
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.urls import reverse
from cuenta.models import Cuenta
from gestor_usuario_roles.models import Estudiante
from .models import Pago
from .forms import PagoForm
from django.contrib.auth.decorators import login_required
from ofipensiones.auth0backend import getRole

@login_required
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

            #pagos = Pago.objects.raw("SELECT * FROM manejador_de_pagos_pago WHERE id = %s", [id])
        else:
            pagos = Pago.objects.all() 

            #pagos = Pago.objects.raw("SELECT * FROM manejador_de_pagos_pago")

        return render(request, 'manejador_de_pagos/pago_list.html', {'pagos': pagos})
    else:
        return HttpResponse("Unauthorized User")


    
@login_required
def obtener_cuentas_por_estudiante(request, estudiante_id):
    cuentas = Cuenta.objects.filter(estudiante_id=estudiante_id)
    data = [{'id': cuenta.id, 'descripcion': cuenta.descripcion} for cuenta in cuentas]
    return JsonResponse(data, safe=False)