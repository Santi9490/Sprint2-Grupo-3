# consultor_base_datos/views.py
from django.http import JsonResponse
import requests
from manejador_estudiantes.ofipensiones import settings
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
    

    
