from django import forms

from .models import Consulta,Usuario,Producto


class PostForm(forms.ModelForm):
    
    class Meta:
        model = Consulta
        fields = ('Rut', 'Nombres','Correo','Telefono','Asunto')
class Postuser(forms.ModelForm):
    class Meta:
        model= Usuario
        fields=('usuario','clave')    

class Postproducto(forms.ModelForm):
    class Meta:
        model= Producto
        fields=('title','text','precio','imagen')         
    