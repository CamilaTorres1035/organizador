from django.db import models

# Create your models here.
class Tarea(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_limite = models.DateField()
    completada = models.BooleanField(default=False)
    
    def __str__(self):
        return self.titulo
    
    class Meta:
        ordering = ['fecha_limite']
