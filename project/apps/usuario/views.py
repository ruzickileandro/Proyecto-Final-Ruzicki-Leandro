from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Usuario
from .forms import UsuarioForm

def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuario/index.html', {'usuarios': usuarios})

def crear_usuario(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("usuario:home")
    else: 
        form = UsuarioForm()
    return render(request, "usuario/crear_usuario.html", {"form": form})