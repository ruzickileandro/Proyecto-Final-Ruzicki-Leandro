from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.contrib.auth import login, authenticate
from apps.usuario.models import Usuario
from apps.evento.models import Evento

from . import forms

def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuario/index.html', {'usuarios': usuarios})

def login_request(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = forms.CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contraseña = form.cleaned_data.get("password")
            user = authenticate(username=usuario, password=contraseña)
            if user is not None:
                login(request, user)
                return render(request, "Home/base.html", {'eventos': Evento.objects.all().order_by('fecha')})
    else:
        form = forms.CustomAuthenticationForm()
    return render(request, "usuario/login.html", {"form": form})

def register(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = forms.CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            mensaje = f"Usuario {username} creado"
            return render(request, "usuario/register.html", {"form": form, "mensaje": mensaje})
    else:
        form = forms.CustomUserCreationForm()
    return render(request, "usuario/register.html", {"form": form})
