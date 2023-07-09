from django.shortcuts import render
from .models import Usuario

def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuario/index.html', {'usuarios': usuarios})