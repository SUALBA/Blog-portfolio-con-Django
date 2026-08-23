from django import forms
from .models import Comentario, Mensaje

# ==========================================================================
# 1. Formulario para la página "Sobre mí" (Más simple y directo)
# ==========================================================================
class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        # En "Sobre mí" a veces solo pedimos nombre y mensaje, o los 4 campos. 
        # Ajusta esto según lo que quieras pedir en esa página específica.
        fields = ['nombre', 'email', 'motivo','mensaje'] 
        widgets = {
                       'nombre': forms.TextInput(attrs={'class': 'cyber-input'}),
            'email': forms.EmailInput(attrs={'class': 'cyber-input'}),
            'motivo': forms.Select(attrs={'class': 'cyber-input'}),
            'mensaje': forms.Textarea(attrs={'rows': 5, 'class': 'cyber-input'}),
        }

            
# ==========================================================================
# 2. Formulario para la página "Contacto" (Completo, con motivo y email)
# ==========================================================================
class ContactoForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['nombre', 'email', 'motivo', 'mensaje']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'placeholder': 'Tu nombre', 
                'class': 'cyber-input'  # ← ESTA CLASE ES LA QUE FUNCIONA
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'tu@email.com', 
                'class': 'cyber-input'
            }),
            'motivo': forms.Select(attrs={
                'class': 'cyber-input'
            }),
            'mensaje': forms.Textarea(attrs={
                'placeholder': 'Cuéntame sobre tu proyecto, auditoría o idea...', 
                'rows': 5, 
                'class': 'cyber-input'
            }),
        }


class ComentarioForm(forms.ModelForm):
    privacidad = forms.BooleanField(
        required=True,
        label='He leído y acepto el aviso de privacidad.'
    )
    # Campo trampa: debe permanecer vacío para una persona real.
    website = forms.CharField(
        required=False,
        label='',
        widget=forms.TextInput(attrs={
            'tabindex': '-1',
            'autocomplete': 'off',
            'class': 'comentario-honeypot',
            'aria-hidden': 'true',
        })
    )

    class Meta:
        model = Comentario
        fields = [
            'nombre',
            'email',
            'contenido',
            'autoriza_mencion',
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'cyber-input',
                'placeholder': 'Tu nombre o alias',
                'autocomplete': 'name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'cyber-input',
                'placeholder': 'tu@email.com (no será público)',
                'autocomplete': 'email',
            }),
            'contenido': forms.Textarea(attrs={
                'class': 'cyber-input',
                'rows': 6,
                'maxlength': 1500,
                'placeholder': 'Comparte tu experiencia o punto de vista…',
            }),
        }

    def clean_website(self):
        value = self.cleaned_data.get('website', '')
        if value:
            raise forms.ValidationError('No se pudo enviar el comentario.')
        return value