from django import forms
from .models import Mensaje

class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['nombre', 'mensaje']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Tu nombre (opcional)', 'class': 'form-input'}),
            'mensaje': forms.Textarea(attrs={'placeholder': 'Deja tu tu mensaje aquí...', 'class': 'form-textarea'}),
            'mensaje': forms.Textarea(attrs={'rows':4}),
        }
        labels = {
            'nombre': 'Tu nombre',
            'email':  'Tu email',
            'mensaje':'Tu mensaje',
        
        }



