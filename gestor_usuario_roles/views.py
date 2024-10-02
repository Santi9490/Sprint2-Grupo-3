from django.http import JsonResponse
from .models import Estudiante

def consulta_estudiantes(request):
    # Obtener los primeros 500 estudiantes
    estudiantes = Estudiante.objects.all()[:500]
    estudiantes_list = list(estudiantes.values('nombre', 'apellido', 'correo', 'fecha_nacimiento'))

    return JsonResponse(estudiantes_list, safe=False)


