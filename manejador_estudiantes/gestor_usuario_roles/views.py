from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .forms import EstudianteForm
from .models import Estudiante
from django.contrib.auth.decorators import login_required
from ofipensiones.auth0backend import getRole

@login_required
def estudiante_list(request):
    role = getRole(request)
    if role == "Rector" or role == "Coordinador":
        estudiantes = Estudiante.objects.all()
        context = {
            'estudiante_list': estudiantes
        }
        return render(request, 'estudiante/estudiantes.html', context)
    else:
        return HttpResponse("Unauthorized User")

@login_required
def estudiante_create(request):
    role = getRole(request)
    if role == "Rector" or role == "Coordinador":
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
    else:
        return HttpResponse("Unauthorized User")






