from django.urls import path, include
from apps.Home.views import home
from apps.evento import views
from .views import crear_evento

app_name = "evento"

urlpatterns = [
    path("", include("Home.urls")),
    path("", home, name="home"),
    path('crear_evento/', crear_evento, name='crear_evento'),
    path('buscar/', views.buscar_eventos, name='buscar_eventos'),
    path('lista_eventos/', views.lista_eventos, name='lista_eventos'),
]