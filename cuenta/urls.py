from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('cuentas/', views.cuenta_list, name='cuenta_list'),
    path('cuenta/create/', views.cuenta_create, name='cuenta_create'),
    path('cuenta/<str:codigo>/', views.cuenta_detalle, name='cuenta_detalle'),
    path('health/', views.health_check, name='health_check'),  # Health Check
]