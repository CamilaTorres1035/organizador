from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tareas, name='lista_tareas'),
    path('tarea/<int:pk>/editar/', views.editar_tarea, name='editar_tarea'),
    path('tarea/<int:pk>/eliminar/', views.eliminar_tarea, name='eliminar_tarea'),
    path('tarea/<int:pk>/completar/', views.marcar_completada, name='marcar_completada'),  # <-- Esta línea es clave
    path('tarea/nueva/', views.registrar_tarea, name='registrar_tarea'),
]