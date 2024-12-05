from django.urls import path
from . import views

urlpatterns = [
    path('/generar_reporte/', views.generar_reporte, name='api_reportes')
]