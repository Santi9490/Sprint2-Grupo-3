from django.http import JsonResponse
from django.shortcuts import render

from gestor_usuario_roles.logic.estudiante_logic import get_estudiante_by_id
from .logic.logic_alarm import get_alarms, get_cuentas_by_estudiante, create_alarm

def alarm_list(request):
    alarms = get_alarms()
    context = list(alarms.values())
    return JsonResponse(context, safe=False)

@csrf_exempt
def generate_alarm(request, estudiante_id):
    estudiante = get_estudiante_by_id(estudiante_id)
    cuentas = get_cuentas_by_estudiante(estudiante_id)
    createAlarm = False
    upperCuenta = None
    for cuenta in cuentas:
        if cuenta.pas_y_salvo == False:
            createAlarm = True
            upperCuenta = cuenta
    if createAlarm:
        alarm = create_alarm(estudiante, upperCuenta, 30)
        return JsonResponse(alarm.toJson(), safe=False)
    else:
        return JsonResponse({'message': 'No alarm created'}, status=200)
