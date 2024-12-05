import requests
from ofipensiones import settings


def obtener_datos_estudiante(estudiante_id):
    """
    Realiza una solicitud al microservicio de estudiantes para obtener los datos del estudiante.
    """
    url = f"{settings.PATH_ESTUDIANTES}/{estudiante_id}/"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error {response.status_code}: {response.text}")
            return None
    except requests.RequestException as e:
        print(f"Error al obtener datos del estudiante: {e}")
        return None
