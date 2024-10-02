from django.urls import path
from . import views

urlpatterns = [
    path('consulta/', views.consulta_estudiantes, name='consulta_estudiantes'),
]
