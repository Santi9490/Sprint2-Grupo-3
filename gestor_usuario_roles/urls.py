from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('estudiantes/', views.estudiante_list, name='estudiantes'),
    path('estudiantecreate/', csrf_exempt(views.estudiante_create), name='estudianteCreate'),
    path('estados-cuenta/', views.estado_cuenta_list, name='estadoCuentaList'),
    path('estado-cuenta/create/', views.estado_cuenta_create, name='estadoCuentaCreate'),
    path('estado-cuenta/<str:codigo>/', views.estado_cuenta_detalle, name='estadoCuentaDetalle'),
    path('health/', views.health_check, name='health_check'),  # Health Check
]

