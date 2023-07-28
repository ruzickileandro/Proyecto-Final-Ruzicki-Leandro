from django.urls import path
from . import views

app_name = 'registro'

urlpatterns = [
    path('registrar/<int:evento_id>/', views.registrar_interes, name='registrar_interes'),
]
