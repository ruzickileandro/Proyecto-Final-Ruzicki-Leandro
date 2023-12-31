from unidecode import unidecode
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpRequest
from .models import Evento, EventoCategoria
from apps.registro.models import Registro
from .forms import EventoForm
from apps.evento.forms import ActualizarEventoForm
from django.db.models import Q

def lista_eventos(request):
    eventos = Evento.objects.all().order_by('fecha')
    context = {
        'eventos': eventos
    }
    return render(request, 'Home/index.html', context)

def lista_categorias(request):
    categorias = EventoCategoria.objects.all()
    eventos_por_categoria = {}
    for categoria in categorias:
        eventos_por_categoria[categoria] = Evento.objects.filter(categoria=categoria)
    context = {
        'eventos_por_categoria': eventos_por_categoria
    }
    return render(request, 'evento/lista_categorias.html', context)

def crear_evento(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = EventoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("Home:home")
    else: 
        form = EventoForm()
    categorias = EventoCategoria.objects.all()
    return render(request, "evento/crear_evento.html", {"form": form, "categorias": categorias})

def buscar_eventos(request):
    query = request.GET.get('q', '')
    eventos = None

    if query:
        query_normalized = query.lower()

        eventos = Evento.objects.filter(
            Q(titulo__icontains=query_normalized) | Q(descripcion__icontains=query_normalized)
        ).distinct()

    return render(request, 'evento/buscar_eventos.html', {'eventos': eventos, 'query': query})

def actualizar_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    if request.method == "POST":
        form = ActualizarEventoForm(request.POST, request.FILES, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('evento:lista_categorias')
    else:
        form = ActualizarEventoForm(instance=evento)
    return render(request, 'evento/actualizar_evento.html', {'form': form})

def eliminar_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    if request.method == 'POST':
        evento.delete()
        return redirect('evento:lista_categorias')
    return render(request, 'eliminar_evento.html', {'evento': evento})

@login_required(login_url=reverse_lazy('usuario:login'))
def detalle_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    usuario = request.user
    registrado = Registro.objects.filter(evento=evento, usuario=usuario).exists()
    return render(request, 'evento/detalle_evento.html', {'evento': evento, 'registrado': registrado})