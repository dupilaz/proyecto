
from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal, name='principal'),
    path('formulario',views.post_new,name='formulario'),
    
]
