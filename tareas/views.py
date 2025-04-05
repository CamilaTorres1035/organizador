from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarea
from django.utils import timezone
from .forms import TareaForm
import datetime

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
    now = datetime.date.today()
    tareas = Tarea.objects.filter(fecha_limite__gte=now).order_by('fecha_limite')
    return render(request, 'tareas/lista.html', {'tareas':tareas})

def editar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('lista_tareas')
    else:
        form = TareaForm(instance=tarea)
    
    return render(request, 'tareas/editar.html', {'form': form})

def eliminar_tarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    if request.method == 'POST':
        tarea.delete()
        return redirect('lista_tareas')
    
    return render(request, 'tareas/eliminar_confirmar.html', {'tarea': tarea})

def marcar_completada(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    if request.method == 'POST':
        tarea.completada = True
        tarea.save()
        return redirect('lista_tareas')
    return render(request, 'tareas/completar.html', {'tarea': tarea})