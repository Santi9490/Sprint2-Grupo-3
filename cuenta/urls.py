from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('cuentas/', views.cuenta_list, name='CuentaList'),
    path('cuenta/create/', views.cuenta_create, name='CuentaCreate'),
    path('cuenta/<str:codigo>/', views.cuenta_detalle, name='CuentaDetalle'),
    path('health/', views.health_check, name='health_check'),  # Health Check
]