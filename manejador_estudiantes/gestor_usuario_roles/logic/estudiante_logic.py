from ..models import Estudiante

def get_estudiantes():
    queryset = Estudiante.objects.all()
    return (queryset)

def get_estudiante_by_id(id):
    queryset = Estudiante.objects.get(id=id)
    return (queryset)

def create_estudiante(form):
    cuenta = form.save()
    cuenta.save()
    return ()