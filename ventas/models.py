from django.db import models
from django.utils import timezone


class Consulta(models.Model):
    
    

    Rut = models.CharField(max_length=10)
                            #widget= forms.TextInput
                           #(attrs={'placeholder':'12345678-9'}))
    Nombres=models.CharField(max_length=50)
                            #widget= forms.TextInput
                           #(attrs={'placeholder':'Juan Perez'}))
    
    Correo=models.EmailField( max_length=50)
                            #widget= forms.TextInput
                           #(attrs={'placeholder':'Ejemplo@Ejemplo.com'}))
    Telefono=models.CharField(max_length=50)
                            #widget= forms.TextInput
                            #(attrs={'placeholder':'987654321'}))
    Asunto=models.CharField(max_length=100)
                            #widget= forms.TextInput
                            #(attrs={'placeholder':'descripcion'}))

    def __str__(self):
        return self.Rut


class Producto(models.Model):
    
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=50)
    precio = models.CharField(max_length=10)
    imagen= models.ImageField(null=True ,blank=True)
        
    
    def __str__(self):
        return self.title        

