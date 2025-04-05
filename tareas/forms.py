from django import forms
from .models import Tarea

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'fecha_limite', 'tipo']
        widgets = {
            'fecha_limite': forms.DateInput(attrs={'type': 'date'})
        }