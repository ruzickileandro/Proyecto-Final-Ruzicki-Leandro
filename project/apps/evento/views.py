from unidecode import unidecode
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Evento
from .forms import EventoForm
#import random

def lista_eventos(request):
    eventos = Evento.objects.all()  # Obtener todos los eventos de la base de datos
    context = {
        'eventos': eventos
    }
    return render(request, 'Home/base.html', context)


def crear_evento(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("evento:home")
    else: 
        form = EventoForm()
    return render(request, "evento/crear_evento.html", {"form": form})



def buscar_eventos(request):
    query = request.GET.get('q', '')
    eventos = None

    if query:
        # Normalizar el texto de búsqueda
        query_normalized = unidecode(query)

        # Realizar la búsqueda sin tener en cuenta las diferencias entre mayúsculas y minúsculas y los acentos
        eventos = Evento.objects.filter(titulo__icontains=query_normalized) | Evento.objects.filter(descripcion__icontains=query_normalized)

    return render(request, 'evento/buscar_eventos.html', {'eventos': eventos, 'query': query})

