from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('', views.producto, name='principal'),
    path('formulario',views.post_new,name='formulario'),
    path('welcome',views.post_pro,name='welcome'),


    #path de los loguin

    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),

]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_URL)
