from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tareas, name='lista_tareas'),
    path('registrar/', views.registrar_tarea, name='registrar_tarea')
]
