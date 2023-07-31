from django.db import models
from apps.evento.models import Evento
from django.contrib.auth import get_user_model

class Registro(models.Model):
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Usuario: {self.usuario} - Evento: {self.evento.titulo}"