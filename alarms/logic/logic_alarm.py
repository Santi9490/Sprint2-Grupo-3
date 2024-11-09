from cuenta.models import Cuenta
from ..models import Alarm

def get_alarms():
    queryset = Alarm.objects.all().order_by('-dateTime')
    return (queryset)

def get_cuentas_by_estudiante(estudiante):
    queryset = Cuenta.objects.filter(estudiante=estudiante).order_by('-dateTime')[:10]
    return (queryset)

def create_alarm(estudiante, cuenta, limitExceeded):
    alarm = Alarm()
    alarm.estudiante = estudiante
    alarm.cuenta = cuenta
    alarm.limitExceeded = limitExceeded
    alarm.save()
    return alarm