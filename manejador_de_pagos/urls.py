# manejador_de_pagos/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('pagocreate/', views.pago_create, name='pagos_create'),  
    path('pagos/', views.pago_list, name='pago_list'),            
    path('pagos/<str:codigo>/', views.pago_list, name='pago_list_estudiante'),  
    path('api/cuentas/<int:estudiante_id>/', views.obtener_cuentas_por_estudiante, name='api_cuentas_por_estudiante'),
]

