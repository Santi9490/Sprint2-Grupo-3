from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('estudiantes/', views.estudiante_list, name='estudiantes'),
    path('estudiantecreate/', csrf_exempt(views.estudiante_create), name='estudianteCreate'),
    path('estudianteslist/', views.estudiantes, name='estudiantesList'),
    path('estudiantenew/', csrf_exempt(views.estudiante_new), name='estudianteNew'),
]

