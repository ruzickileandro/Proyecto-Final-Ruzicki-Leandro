from django.urls import path
from apps.evento import views

app_name = "evento"

urlpatterns = [
    path('crear_evento/', views.crear_evento, name='crear_evento'),
    path('buscar/', views.buscar_eventos, name='buscar_eventos'),
    path('lista_eventos/', views.lista_eventos, name='lista_eventos'),
    path('lista_categorias/', views.lista_categorias, name='lista_categorias'),
    path('actualizar_evento/<int:evento_id>/', views.actualizar_evento, name='actualizar_evento'),
    path('eliminar/<int:evento_id>/', views.eliminar_evento, name='eliminar_evento'),
]