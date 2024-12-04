# manejador_de_pagos/views.py
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.urls import reverse
import requests
from cuenta.models import Cuenta
from manejador_integraciones_contables.ofipensiones import settings
from .models import Pago
from .forms import PagoForm
from django.contrib.auth.decorators import login_required
from ofipensiones.auth0backend import getRole
from consultor_base_datos.views import generar_reporte
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.pdfgen import canvas

def get_estudiantes():
    """Obtiene todos los estudiantes del microservicio"""
    try:
        response = requests.get(settings.PATH_ESTUDIANTES, headers={"Accept": "application/json"})
        response.raise_for_status() 
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener estudiantes: {e}")
        return [] 

def get_estudiante_por_codigo(codigo):
    """Obtiene un estudiante por su código"""
    estudiantes = get_estudiantes()
    return next((estudiante for estudiante in estudiantes if estudiante['codigo'] == codigo), None)


def pago_create(request):
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
    



def pago_list(request, id=None):
    
    if id:
        pagos = Pago.objects.filter(id=id)
    else:
        pagos = Pago.objects.all()

    return render(request, 'manejador_de_pagos/pago_list.html', {'pagos': pagos})
    

def pago_list(request):
    if id:
        pagos = Pago.objects.filter(id=id)
    else:
        pagos = Pago.objects.all()

    return render(request, 'manejador_de_pagos/pago_list.html', {'pagos': pagos})
   

    
def obtener_cuentas_por_estudiante(request, estudiante_codigo):
    estudiante = get_estudiante_por_codigo(estudiante_codigo)
    
    if estudiante is None:
        return JsonResponse({"error": "Estudiante no encontrado"}, status=404)

    cuentas = Cuenta.objects.filter(estudiante_codigo=estudiante_codigo)
    data = [{
        'id': cuenta.id,
        'descripcion': cuenta.descripcion,
        'monto_pagado': cuenta.monto_pagado,
        'saldo_pendiente': cuenta.saldo_pendiente
    } for cuenta in cuentas]

    return JsonResponse(data, safe=False)

def generar_reporte_pdf(request):
    """Genera el reporte en formato PDF con las cuentas de los estudiantes"""
    try:
        
        estudiantes_response = generar_reporte(request)
        estudiantes = estudiantes_response.json()
    except Exception as e:
        print(f"Error al obtener el reporte de estudiantes: {e}")
        return HttpResponse("Error al obtener datos", status=500)

    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte_estudiantes.pdf"'

   
    c = canvas.Canvas(response, pagesize=letter)
    width, height = letter

   
    c.setFont("Helvetica-Bold", 16)
    c.drawString(200, height - 40, "Reporte de Cuentas de Estudiantes")

    
    y_position = height - 80

    
    c.setFont("Helvetica-Bold", 10)
    c.drawString(30, y_position, "Estudiante")
    c.drawString(200, y_position, "Código")
    c.drawString(350, y_position, "Cuenta Descripción")
    c.drawString(500, y_position, "Monto Pagado")
    c.drawString(600, y_position, "Saldo Pendiente")
    
    y_position -= 20

    
    c.setFont("Helvetica", 10)
    for estudiante in estudiantes:
        cuentas = estudiante.get("cuentas", [])

        for cuenta in cuentas:
            c.drawString(30, y_position, f"{estudiante['nombre']} {estudiante['apellido']}")
            c.drawString(200, y_position, str(estudiante["codigo"]))
            c.drawString(350, y_position, cuenta.get("descripcion", ""))
            c.drawString(500, y_position, str(cuenta.get("monto_pagado", 0)))
            c.drawString(600, y_position, str(cuenta.get("saldo_pendiente", 0)))
            y_position -= 15

            
            if y_position < 50:
                c.showPage()
                y_position = height - 40
                c.setFont("Helvetica-Bold", 10)
                c.drawString(30, y_position, "Estudiante")
                c.drawString(200, y_position, "Código")
                c.drawString(350, y_position, "Cuenta Descripción")
                c.drawString(500, y_position, "Monto Pagado")
                c.drawString(600, y_position, "Saldo Pendiente")
                y_position -= 20
    c.save()
    
    return response


