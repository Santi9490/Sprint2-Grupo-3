# consultor_base_datos/views.py
from django.http import JsonResponse
import requests
from manejador_integraciones_contables.cuenta.models import Cuenta
from ofipensiones import settings
from manejador_de_pagos.views import obtener_cuentas_por_estudiante

reporte_cache = None

def obtener_estudiantes():
    """Obtiene los estudiantes desde el microservicio de estudiantes"""
    try:
        r = requests.get(settings.PATH_ESTUDIANTES, headers={"Accept": "application/json"})
        return r.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener estudiantes: {e}")
        return []
    
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

def generar_reporte(request):
    """Genera el reporte de todos los estudiantes con sus cuentas, llamando directamente a la vista del manejador de pagos"""

    global reporte_cache

    if reporte_cache:
        return JsonResponse(reporte_cache, safe=False)
    
    estudiantes = obtener_estudiantes()

    for estudiante in estudiantes:
        estudiante["cuentas"] = obtener_cuentas_por_estudiante(estudiante["codigo"])

    
    reporte_cache = estudiantes

    return JsonResponse(estudiantes, safe=False)
    

    
