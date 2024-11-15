from cuenta.models import Cuenta


def get_cuentas_by_estudiante(estudiante):
    queryset = Cuenta.objects.filter(estudiante=estudiante).order_by('-fecha_actualizacion')[:10]
    return queryset