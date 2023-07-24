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
from apps.usuario.views import login_request

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_request, name="login"),
    path('logout/', LogoutView.as_view(template_name='usuario/logout.html'), name="logout"),
    path('', lista_eventos, name='home'),
    path('crear_usuario/', crear_usuario, name='crear_usuario'),
    path('crear_evento/', crear_evento, name='crear_eventos'),
    path('buscar_eventos/', buscar_eventos, name='buscar_eventos'),
    path('', include('apps.evento.urls', namespace='lista_eventos')),
     
]