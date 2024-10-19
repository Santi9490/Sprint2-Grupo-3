from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import EstudianteForm
from .models import Estudiante
from concurrent.futures import ThreadPoolExecutor

# Función para listar estudiantes
def estudiante_list(request):
    from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import EstudianteForm
from .models import Estudiante

# Función para listar estudiantes
def estudiante_list(request):
    estudiantes = Estudiante.objects.all()
    context = {
        'estudiante_list': estudiantes
    }
    return render(request, 'estudiante/estudiantes.html', context)

# Función para crear un nuevo estudiante
def estudiante_create(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save() 
            messages.add_message(request, messages.SUCCESS, 'Estudiante creado exitosamente')
            return HttpResponseRedirect(reverse('estudianteCreate'))
        else:
            print(form.errors)
    else:
        form = EstudianteForm()

    context = {
        'form': form,
    }
    return render(request, 'estudiante/estudianteCreate.html', context)



