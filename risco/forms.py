from django import forms
from .models import Cotizacion
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .backends import EmailBackend


class FormularioRegistro(UserCreationForm):
    email = forms.EmailField(required=True, label="Correo Electrónico")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'Nombre de usuario',
            'email': 'Email',
            'password1': 'Contraseña',
            'password2': 'Confirmar Contraseña',
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label="Correo Electrónico")

class CotizacionForm(forms.ModelForm):
    class Meta:
        model = Cotizacion
        fields = ['nombre', 'correo', 'telefono', 'mensaje']
        labels = {
            'nombre': 'Nombre',
            'email': 'Email',
            'telefono': 'Teléfono',
            'mensaje': 'Comentarios o preguntas',    
        }
        