from django.urls import path
from apps.evento import views

app_name = "evento"

urlpatterns = [
    path('crear_evento/', views.crear_evento, name='crear_evento'),
    path('buscar/', views.buscar_eventos, name='buscar_eventos'),
    path('lista_eventos/', views.lista_eventos, name='lista_eventos'),
]