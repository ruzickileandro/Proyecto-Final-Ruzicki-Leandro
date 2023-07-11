from django.urls import path, include
from .views import crear_usuario

app_name = "usuario"

urlpatterns = [
    path("", include("Home.urls")),
    path('crear/', crear_usuario, name='crear'),
]