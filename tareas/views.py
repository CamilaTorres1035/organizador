from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarea
from django.utils import timezone
from .forms import TareaForm
from datetime import date, timedelta
from django.db.models import Q

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
    now = date.today()
    busqueda = request.GET.get('busqueda')
    filtro = request.GET.get('filtro')
    if busqueda:
        if filtro == "hoy":
            tareas = Tarea.objects.filter(Q(titulo__icontains=busqueda) | Q(descripcion__icontains=busqueda), fecha_limite=now).order_by('fecha_limite')
        elif filtro == "semana":
            semana = now + timedelta(days=7)
            tareas = Tarea.objects.filter(Q(titulo__icontains=busqueda) | Q(descripcion__icontains=busqueda), fecha_limite__range=(now, semana)).order_by('fecha_limite')
        elif filtro == "incompleto":
            tareas = Tarea.objects.filter(Q(titulo__icontains=busqueda) | Q(descripcion__icontains=busqueda), completada = False, fecha_limite__gte=now).order_by('fecha_limite')
        else:
            tareas = Tarea.objects.filter(Q(titulo__icontains=busqueda) | Q(descripcion__icontains=busqueda), fecha_limite__gte=now).order_by('fecha_limite')
    else:
        if filtro == "hoy":
            tareas = Tarea.objects.filter(fecha_limite=now).order_by('fecha_limite')
        elif filtro == "semana":
            semana = now + timedelta(days=7)
            tareas = Tarea.objects.filter(fecha_limite__range=(now, semana)).order_by('fecha_limite')
        elif filtro == "incompleto":
            tareas = Tarea.objects.filter(completada = False, fecha_limite__gte=now).order_by('fecha_limite')
        else:
            tareas = Tarea.objects.filter(fecha_limite__gte=now).order_by('fecha_limite')
    return render(request, 'tareas/lista.html', {'tareas': tareas, 'filtro': filtro})

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