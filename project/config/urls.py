"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from apps.usuario.views import crear_usuario
from apps.evento.views import crear_evento
from apps.evento.views import buscar_eventos
from apps.evento.views import lista_eventos
from apps.Home.views import home
#from apps.evento import views as evento_views
#from apps.usuario import views as usuario_views
from apps.registro import views as registro_views
#from apps.Home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', lista_eventos, name='home'),
    #path('home/', home, name="home"),

    path('crear_usuario/', crear_usuario, name='crear_usuario'),
    path('usuario/', include('apps.usuario.urls', namespace='crear_usuario')),

    path('crear_evento/', crear_evento, name='crear_evento'),
    path('evento/', include('apps.evento.urls', namespace='crear_evento')),

    path('eventos/', include('apps.evento.urls', namespace='buscar_eventos')),
    path('buscar_eventos/', buscar_eventos, name='buscar_eventos'),

    path('lista/', include('apps.evento.urls', namespace='lista_eventos')),
    #path('eventos/', evento_views.lista_eventos, name='lista_eventos'),
    #path('usuarios/', usuario_views.lista_usuarios, name='lista_usuarios'),
    path('registros/', registro_views.lista_registros, name='lista_registros'),
    #path('registro/', views.registro_view, name='registro'),
    #path('lista_eventos/', lista_eventos, name='lista_eventos'),
]

