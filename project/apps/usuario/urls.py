from django.urls import path, include
from .views import crear_usuario
from apps.Home import views

app_name = "usuario"

urlpatterns = [
    path("", include("Home.urls")),
    path('', views.home, name='home'),
    path('crear_usuario/', crear_usuario, name='crear_usuario'),
]