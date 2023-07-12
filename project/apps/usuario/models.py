from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    contraseña = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"