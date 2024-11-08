from concurrent.futures import ThreadPoolExecutor
import json
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

from gestor_usuario_roles.models import Estudiante
from .forms import ColegioForm
from .models import Colegio

# Función para listar colegios
def colegio_list(request):
    colegios = Colegio.objects.all()
    context = {
        'colegio_list': colegios
    }
    return render(request, 'colegio/colegios.html', context)

# Función para crear un nuevo colegio

executor = ThreadPoolExecutor(max_workers=56)
def colegio_create(request):
    if request.method == 'POST':
        form = ColegioForm(request.POST)
        if form.is_valid():
            future = executor.submit(form.save)
            future.result()

            return HttpResponseRedirect(reverse('colegioCreate'))
        else:
            print(form.errors)
    else:
        form = ColegioForm()

    context = {
        'form': form,
    }
    return render(request, 'colegio/colegioCreate.html', context)