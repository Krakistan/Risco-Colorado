from django import forms
from django.forms import ModelForm


class Inicio(forms.Form):
    correo = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class Registrarse(forms.Form):
    nombre = forms.CharField(label='Nombre')
    correo = forms.EmailField(label='Correo')
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')

class Cotizacion(forms.Form):
    nombre = forms.CharField(label='Nombre')
    correo = forms.EmailField(label='Correo')
    telefono = forms.CharField(label='Telefono')
    mensaje = forms.CharField(label='mensaje')
    
    def __str__(self):
        return self.nombre