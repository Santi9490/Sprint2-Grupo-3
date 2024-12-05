from django.http import JsonResponse
from pymongo import MongoClient
from django.contrib.auth.decorators import login_required
from ofipensiones import settings
from ofipensiones.auth0backend import getRole

def get_mongo_client():
    """Crea un cliente MongoDB."""
    return MongoClient(settings.MONGO_CLI)

@login_required
def estudiante_list(request):
    """Devuelve todos los estudiantes de la base de datos NoSQL (MongoDB)."""
    role = getRole(request)
    if role in ["Rector", "Coordinador"]:
        client = get_mongo_client()
        db = client.gestor_usuario_roles_db
        estudiantes_collection = db['estudiantes']
        estudiantes = estudiantes_collection.find().sort([('apellido', 1)])
        result = [
            {
                'id': str(estudiante['_id']),
                'nombre': estudiante['nombre'],
                'apellido': estudiante['apellido'],
                'codigo': estudiante['codigo'],
                'fecha_nacimiento': estudiante['fecha_nacimiento'],
                'numero_acudiente': estudiante['numero_acudiente'],
                'direccion': estudiante['direccion'],
            }
            for estudiante in estudiantes
        ]
        client.close()
        return JsonResponse(result, safe=False)
    else:
        return JsonResponse({"error": "Unauthorized User"}, status=403)

@login_required
def estudiante_create(request):
    """Crea un nuevo estudiante en la base de datos NoSQL (MongoDB)."""
    role = getRole(request)
    if role in ["Rector", "Coordinador"]:
        if request.method == "POST":
            data = {
                'nombre': request.POST.get('nombre'),
                'apellido': request.POST.get('apellido'),
                'codigo': request.POST.get('codigo'),
                'fecha_nacimiento': request.POST.get('fecha_nacimiento'),
                'numero_acudiente': request.POST.get('numero_acudiente'),
                'direccion': request.POST.get('direccion'),
            }

            client = get_mongo_client()
            db = client.gestor_usuario_roles_db
            estudiantes_collection = db['estudiantes']

            # Verifica si el estudiante ya existe por el campo 'codigo'
            existing_estudiante = estudiantes_collection.find_one({'codigo': data['codigo']})
            if existing_estudiante:
                client.close()
                return JsonResponse({"error": "Estudiante con ese código ya existe"}, status=400)

            # Insertamos el nuevo estudiante en MongoDB
            result = estudiantes_collection.insert_one(data)
            response_data = {
                "id": str(result.inserted_id),
                "message": "Estudiante creado exitosamente",
            }
            client.close()
            return JsonResponse(response_data, safe=False)
        else:
            return JsonResponse({"error": "Invalid request method"}, status=400)
    else:
        return JsonResponse({"error": "Unauthorized User"}, status=403)

def estudiantes(request):
    """Devuelve todos los estudiantes de la base de datos NoSQL (MongoDB)."""
    client = get_mongo_client()
    db = client.gestor_usuario_roles_db
    estudiantes_collection = db['estudiantes']

    estudiantes = estudiantes_collection.find().sort([('nombre', 1)])  # Ordenar por 'nombre'
    result = [
        {
            'id': str(estudiante['_id']),
            'nombre': estudiante['nombre'],
            'apellido': estudiante['apellido'],
            'codigo': estudiante['codigo'],
            'fecha_nacimiento': estudiante['fecha_nacimiento'],
            'numero_acudiente': estudiante['numero_acudiente'],
            'direccion': estudiante['direccion'],
        }
        for estudiante in estudiantes
    ]
    client.close()
    return JsonResponse(result, safe=False)

def estudiante_new(request):
    """Crea un nuevo estudiante en la base de datos NoSQL (MongoDB)."""
    
    if request.method == "POST":
        data = {
            'nombre': request.POST.get('nombre'),
            'apellido': request.POST.get('apellido'),
            'codigo': request.POST.get('codigo'),
            'fecha_nacimiento': request.POST.get('fecha_nacimiento'),
            'numero_acudiente': request.POST.get('numero_acudiente'),
            'direccion': request.POST.get('direccion'),
        }

        client = get_mongo_client()
        db = client.gestor_usuario_roles_db
        estudiantes_collection = db['estudiantes']

        # Verifica si el estudiante ya existe por el campo 'codigo'
        existing_estudiante = estudiantes_collection.find_one({'codigo': data['codigo']})
        if existing_estudiante:
            client.close()
            return JsonResponse({"error": "Estudiante con ese código ya existe"}, status=400)

        # Insertamos el nuevo estudiante en MongoDB
        result = estudiantes_collection.insert_one(data)
        response_data = {
            "id": str(result.inserted_id),
            "message": "Estudiante creado exitosamente",
        }
        client.close()
        return JsonResponse(response_data, safe=False)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=400)
    

def index(request):
    """Vista de inicio."""
    return JsonResponse({"message": "Bienvenido a la API de Ofipensiones"}, safe=False)





