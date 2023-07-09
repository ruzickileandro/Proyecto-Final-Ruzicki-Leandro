from django.db import models
from apps.evento.models import Evento
from apps.usuario.models import Usuario

class Registro(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)