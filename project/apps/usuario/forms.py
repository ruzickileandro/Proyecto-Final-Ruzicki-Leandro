from django import forms
from apps.usuario.models import Usuario
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'usuario', 'email', 'contraseña']

def usuarioFormulario(request):
 
      if request.method == "POST":
 
            miFormulario = UsuarioForm(request.POST)
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  usuario = Usuario(nombre=informacion["nombre"],
                                   apellido=informacion["apellido"],
                                   usuario=informacion["usuario"],
                                   email=informacion["email"],
                                   contraseña=informacion["contraseña"])
                  usuario.save()
                  return render(request, "Home/base.html")
      else:
            miFormulario = UsuarioForm()
 
      return render(request, "usuario/crear_usuario.html", {"miFormulario": miFormulario})

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username", "password"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "password": forms.PasswordInput(attrs={"class": "form-control"}),
        }