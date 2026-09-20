from django import forms 
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Reunion, TipoReunion
 
class ReunionForm(forms.ModelForm): 
    class Meta: 
        model = Reunion 
        fields = [ 
            'tipo', 
            'titulo', 
            'fecha', 
            'hora', 
            'lugar', 
            'participantes', 
            'observaciones', 
            'estado', 
        ] 
        widgets = { 
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}), 
            'hora': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}), 
            'participantes': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}), 
            'observaciones': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}), 
        } 
 
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs) 
        for field in self.fields.values(): 
            field.widget.attrs.setdefault('class', 'form-control') 
            self.fields['fecha'].widget.attrs['min'] = timezone.now().date().isoformat()

    # --- Para desafío Agregar ---
    def clean_fecha(self):
        fecha = self.cleaned_data.get('fecha')
        # Comprueba si la fecha ingresada es menor a la fecha actual de hoy
        if fecha and fecha < timezone.now().date():
            raise ValidationError("La fecha de la reunión no puede ser anterior a la fecha actual.")
        return fecha

class TipoReunionForm(forms.ModelForm):
    class Meta:
        model = TipoReunion
        fields = '__all__'

    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs) 
        for field in self.fields.values(): 
            field.widget.attrs.setdefault('class', 'form-control')