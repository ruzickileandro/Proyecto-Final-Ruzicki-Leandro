from django.db import models

class EventoCategoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Evento(models.Model):

    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateField()
    categoria = models.ForeignKey(EventoCategoria, on_delete=models.CASCADE)
    def __str__(self):
       return f"{self.fecha.strftime('%d/%m/%Y')} : {self.titulo}"
    