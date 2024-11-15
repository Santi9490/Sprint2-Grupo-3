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
def pago_list(request, codigo=None):
    role = getRole(request)
    if role in ["Rector", "Coordinador", "Secretaria"]:
        estudiante = None
        pagos = Pago.objects.all()

        if codigo:
            estudiante = get_object_or_404(Estudiante, codigo=codigo)
            pagos = pagos.filter(estudiante=estudiante)

        fecha_inicio = request.GET.get("fecha_inicio")
        fecha_fin = request.GET.get("fecha_fin")
        monto_min = request.GET.get("monto_min")
        monto_max = request.GET.get("monto_max")

        if fecha_inicio and fecha_fin:
            pagos = pagos.filter(fecha_pago__range=[fecha_inicio, fecha_fin])
        if monto_min:
            pagos = pagos.filter(monto__gte=monto_min)
        if monto_max:
            pagos = pagos.filter(monto__lte=monto_max)

        context = {
            'pagos': pagos,
            'estudiante': estudiante,
            'filtros': {
                'fecha_inicio': fecha_inicio,
                'fecha_fin': fecha_fin,
                'monto_min': monto_min,
                'monto_max': monto_max,
            },
        }
        return render(request, 'manejador_de_pagos/pago_list.html', context)
    else:
        return HttpResponse("Unauthorized User")


    
@login_required
def obtener_cuentas_por_estudiante(request, estudiante_id):
    cuentas = Cuenta.objects.filter(estudiante_id=estudiante_id)
    data = [{'id': cuenta.id, 'descripcion': cuenta.descripcion} for cuenta in cuentas]
    return JsonResponse(data, safe=False)