from django.shortcuts import render
from .models import Registro

def lista_registros(request):
    registros = Registro.objects.all()
    return render(request, 'registro/lista_registros.html', {'registros': registros})