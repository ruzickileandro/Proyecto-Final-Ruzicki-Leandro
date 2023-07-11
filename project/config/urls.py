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
from apps.usuario import views
from apps.Home.views import home
#from apps.evento import views as evento_views
#from apps.usuario import views as usuario_views
#from apps.registro import views as registro_views
#from apps.Home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name="home"),
    #path('eventos/', evento_views.lista_eventos, name='lista_eventos'),
    #path('usuarios/', usuario_views.lista_usuarios, name='lista_usuarios'),
    #path('registros/', registro_views.lista_registros, name='lista_registros'),
    #path('registro/', views.registro_view, name='registro'),
    path('crear/', views.crear_usuario, name='crear'),
]

