from django.shortcuts import render, redirect
from .models import Tarea
from django.utils import timezone

# Create your views here.
def registrar_tarea(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        fecha_limite = request.POST.get('fecha_limite')
        
        Tarea.objects.create(titulo=titulo, descripcion=descripcion, fecha_limite=fecha_limite)
        
        return redirect('lista_tareas')
    
    return render(request, 'tareas/registrar.html')

def lista_tareas(request):
    tareas = Tarea.objects.all().order_by('-fecha_limite')
    return render(request, 'tareas/lista.html', {'tareas':tareas})

