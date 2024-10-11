from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('colegios/', views.colegio_list, name='colegios'),
    path('colegiocreate/', csrf_exempt(views.colegio_create), name='colegioCreate'),
]
