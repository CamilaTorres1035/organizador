from django.shortcuts import render, redirect
from .models import Tarea
from django.utils import timezone
from .forms import TareaForm

# Create your views here.
def registrar_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tareas')
    else:
        form = TareaForm()
        
    return render(request, 'tareas/registrar.html',{'form': form})

def lista_tareas(request):
    tareas = Tarea.objects.all().order_by('-fecha_limite')
    return render(request, 'tareas/lista.html', {'tareas':tareas})

