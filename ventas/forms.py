from django import forms

from .models import Consulta,Producto


class PostForm(forms.ModelForm):
    
    class Meta:
        model = Consulta
        fields = ('Rut', 'Nombres','Correo','Telefono','Asunto')


class Postproducto(forms.ModelForm):
    class Meta:
        model= Producto
        fields=('title','text','precio','imagen')         
    