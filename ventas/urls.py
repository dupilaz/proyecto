from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal, name='principal'),
    path('formulario',views.post_new,name='formulario'),


    #path de los loguin

    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),

    path('admin/', admin.site.urls),
]
