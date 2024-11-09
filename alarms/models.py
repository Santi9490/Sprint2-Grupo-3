from django.db import models
from gestor_usuario_roles.models import Estudiante
from cuenta.models import Cuenta

class Alarm(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, default=None)
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE, default=None)
    limitExceeded = models.FloatField(null=True, blank=True, default=None)
    dateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{"estudiante": %s, "cuenta": %s, "limitExceeded": %s, "dateTime": %s}' % (self.estudiante.name, self.cuenta, self.limitExceeded, self.dateTime)
    
    def toJson(self):
        alarm = {
            'id': self.id,
            'estudiante': self.estudiante.nombre,
            'cuenta': self.cuenta.pas_y_salvo,
            'dateTime': self.dateTime,
            'limitExceeded': self.limitExceeded
        }
        return alarm
