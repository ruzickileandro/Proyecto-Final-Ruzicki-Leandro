from django.urls import path
from . import views

app_name = 'registro'

urlpatterns = [
    path('registrar/<int:evento_id>/', views.registrar_interes, name='registrar_interes'),
    path('lista_usuarios_eventos/', views.lista_usuarios_eventos, name='lista_usuarios_eventos'),
    path('eliminar_registro/<int:usuario_id>/<int:evento_id>/', views.eliminar_registro, name='eliminar_registro'),
    path('quitar_interes/<int:evento_id>/', views.quitar_interes, name='quitar_interes'),
]
