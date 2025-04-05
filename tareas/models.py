from django.db import models

# Create your models here.
class TiposTarea(models.TextChoices):
    TAREA = 'T', 'Tarea'
    PARCIAL = 'P', 'Parcial'
    QUIZ = 'Q', 'Quiz'

class Tarea(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_limite = models.DateField()
    completada = models.BooleanField(default=False)
    tipo = models.CharField(max_length=1, choices=TiposTarea.choices, default=TiposTarea.TAREA)
    
    def __str__(self):
        return self.titulo
    
    class Meta:
        ordering = ['fecha_limite']
