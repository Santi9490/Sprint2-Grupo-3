from django.conf import settings
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from pymongo import MongoClient
from .forms import EstudianteForm
from .models import Estudiante
from django.contrib.auth.decorators import login_required
from ofipensiones.auth0backend import getRole

client = MongoClient(settings.MONGO_CLI)
db = client.gestor_usuario_roles_db
estudiantes_collection = db['estudiantes']

@login_required
def estudiante_list(request):
    """Devuelve todos los estudiantes de la base de datos NoSQL (MongoDB)"""
    role = getRole(request)
    if role == "Rector" or role == "Coordinador":
        estudiantes = estudiantes_collection.find()
        result = []
        for estudiante in estudiantes:
            result.append({
                'id': str(estudiante['_id']),
                'nombre': estudiante['nombre'],
                'apellido': estudiante['apellido'],
                'codigo': estudiante['codigo'],
                'fecha_nacimiento': estudiante['fecha_nacimiento'],
                'numero_acudiente': estudiante['numero_acudiente'],
                'direccion': estudiante['direccion']
            })
        client.close()
        return JsonResponse(result, safe=False)
    else:
        return JsonResponse({"error": "Unauthorized User"}, status=403)

@login_required
def estudiante_create(request):
    """Crea un nuevo estudiante en la base de datos NoSQL (MongoDB)"""
    role = getRole(request)
    if role == "Rector" or role == "Coordinador":
        if request.method == "POST":
            data = {
                'nombre': request.POST['nombre'],
                'apellido': request.POST['apellido'],
                'codigo': request.POST['codigo'],
                'fecha_nacimiento': request.POST['fecha_nacimiento'],
                'numero_acudiente': request.POST['numero_acudiente'],
                'direccion': request.POST['direccion'],
            }
            
            # Insertamos el nuevo estudiante en MongoDB
            result = estudiantes_collection.insert_one(data)
            
            response_data = {
                "id": str(result.inserted_id),
                "message": "Estudiante creado exitosamente"
            }
            client.close()
            return JsonResponse(response_data, safe=False)
        else:
            return JsonResponse({"error": "Invalid request method"}, status=400)
    else:
        return JsonResponse({"error": "Unauthorized User"}, status=403)


def estudiantes(request):
    """Devuelve todos los estudiantes de la base de datos NoSQL (MongoDB)"""
    estudiantes = estudiantes_collection.find()
    result = []
    for estudiante in estudiantes:
        result.append({
            'id': str(estudiante['_id']),
            'nombre': estudiante['nombre'],
            'apellido': estudiante['apellido'],
            'codigo': estudiante['codigo'],
            'fecha_nacimiento': estudiante['fecha_nacimiento'],
            'numero_acudiente': estudiante['numero_acudiente'],
            'direccion': estudiante['direccion']
        })
    client.close()
    return JsonResponse(result, safe=False)

def estudiante_new(request):
    if request.method == "POST":
        data = {
            'nombre': request.POST['nombre'],
            'apellido': request.POST['apellido'],
            'codigo': request.POST['codigo'],
            'fecha_nacimiento': request.POST['fecha_nacimiento'],
            'numero_acudiente': request.POST['numero_acudiente'],
            'direccion': request.POST['direccion'],
        }
        
        # Insertamos el nuevo estudiante en MongoDB
        result = estudiantes_collection.insert_one(data)
        
        response_data = {
            "id": str(result.inserted_id),
            "message": "Estudiante creado exitosamente"
        }
        client.close()
        return JsonResponse(response_data, safe=False)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=400)



