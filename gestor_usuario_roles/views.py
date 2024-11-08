from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .forms import EstadoCuentaForm, EstudianteForm
from .models import EstadoCuenta, Estudiante

# Función para listar estudiantes
def estudiante_list(request):
    estudiantes = Estudiante.objects.all()
    context = {
        'estudiante_list': estudiantes
    }
    return render(request, 'estudiante/estudiantes.html', context)

# Función para crear un nuevo estudiante
def estudiante_create(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save() 
            messages.add_message(request, messages.SUCCESS, 'Estudiante creado exitosamente')
            return HttpResponseRedirect(reverse('estudianteCreate'))
        else:
            print(form.errors)
    else:
        form = EstudianteForm()

    context = {
        'form': form,
    }
    return render(request, 'estudiante/estudianteCreate.html', context)


def estado_cuenta_list(request):
    estados_cuenta = EstadoCuenta.objects.select_related('estudiante').all()
    context = {
        'estado_cuenta_list': estados_cuenta
    }
    return render(request, 'estudiante/estados_cuenta.html', context)

# Función para crear un nuevo estado de cuenta
def estado_cuenta_create(request):
    if request.method == 'POST':
        form = EstadoCuentaForm(request.POST)
        if form.is_valid():
            form.save() 
            messages.add_message(request, messages.SUCCESS, 'Estado de cuenta creado exitosamente')
            return HttpResponseRedirect(reverse('estadoCuentaCreate'))
        else:
            print(form.errors)
    else:
        form = EstadoCuentaForm()

    context = {
        'form': form,
    }
    return render(request, 'estudiante/estadoCuentaCreate.html', context)

# Función para ver el estado de cuenta de un solo estudiante con todos sus registros
def estado_cuenta_detalle(request, codigo):
    estudiante = get_object_or_404(Estudiante, codigo=codigo)
    estados_cuenta = EstadoCuenta.objects.filter(estudiante=estudiante)
    context = {
        'estudiante': estudiante,
        'estados_cuenta': estados_cuenta
    }
    return render(request, 'estudiante/estado_cuenta_detalle.html', context)

def health_check(request):
    # Inicializa los estados como 'ok'
    db_status = 'ok'
    recibo_status = 'ok'
    estado_cuenta_status = 'ok'
    
    # Verifica conexión a la base de datos
    try:
        Estudiante.objects.first()
    except Exception as e:
        db_status = 'error'

    # Verifica la funcionalidad de generación de recibos
    try:
        EstadoCuenta.objects.filter(descripcion='Recibo de prueba').first()
    except Exception as e:
        recibo_status = 'error'

    # Verifica la funcionalidad de consulta de estado de cuenta
    try:
        EstadoCuenta.objects.filter(estudiante__codigo='0000').first()
    except Exception as e:
        estado_cuenta_status = 'error'

    # Determina el estado general de la aplicación
    app_status = 'ok' if all(status == 'ok' for status in [db_status, recibo_status, estado_cuenta_status]) else 'error'

    # Devuelve un JSON con el estado de cada componente y el estado general
    return JsonResponse({
        'app_status': app_status,
        'db_status': db_status,
        'recibo_status': recibo_status,
        'estado_cuenta_status': estado_cuenta_status
    })



