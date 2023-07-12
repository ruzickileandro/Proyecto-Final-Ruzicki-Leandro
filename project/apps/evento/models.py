from django.db import models

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateField()
    categoria = models.TextField()
    def __str__(self):
       return f"{self.fecha.strftime('%d/%m/%Y')} : {self.titulo}"
    