from django import forms
from .models import Registrado,Libro,Resena

class RegistradoForm(forms.ModelForm):
    class Meta:
        model = Registrado
        fields = ["usuario","password", "correo",]


class FormLogin(forms.Form):
    usuario=forms.CharField(max_length=70)
    password=forms.CharField(max_length=70)



class FormBusqueda(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'
