from django import forms

from .models import consulta,usuario


class PostForm(forms.ModelForm):
    
    class Meta:
        model = consulta
        fields = ('Rut', 'Nombres','Correo','Telefono','Asunto')
class Postuser(forms.ModelForm):
    class meta:
        model= usuario
        fields=('usuario','clave')        
    