from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from cuenta.models import Cuenta
from gestor_usuario_roles.models import Estudiante
from cuenta.forms import CuentaForm

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
            return HttpResponseRedirect(reverse('cuentaCreate'))
        else:
            print(form.errors)
    else:
        form = CuentaForm()

    context = {
        'form': form,
    }
    return render(request, 'cuenta/cuentaCreate.html', context)

# Función para ver el estado de cuenta de un solo estudiante con todos sus registros
def cuenta_detalle(request, codigo):
    estudiante = get_object_or_404(Estudiante, codigo=codigo)
    estados_cuenta = Cuenta.objects.filter(estudiante=estudiante)
    context = {
        'estudiante': estudiante,
        'estados_cuenta': estados_cuenta
    }
    return render(request, 'cuenta/cuenta_detalle.html', context)

def health_check(request):
    db_status = 'ok'
    recibo_status = 'ok'
    estado_cuenta_status = 'ok'
    
    try:
        Estudiante.objects.first()
    except Exception as e:
        db_status = 'error'
    try:
        Cuenta.objects.filter(descripcion='Recibo de prueba').first()
    except Exception as e:
        recibo_status = 'error'
    try:
        Cuenta.objects.filter(estudiante__codigo='0000').first()
    except Exception as e:
        estado_cuenta_status = 'error'

    app_status = 'ok' if all(status == 'ok' for status in [db_status, recibo_status, estado_cuenta_status]) else 'error'

    
    return JsonResponse({
        'app_status': app_status,
        'db_status': db_status,
        'recibo_status': recibo_status,
        'estado_cuenta_status': estado_cuenta_status
    })
