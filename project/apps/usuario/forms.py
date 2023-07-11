from django import forms
from apps.usuario.models import Usuario
from django.shortcuts import render

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'email']

def usuarioFormulario(request):
 
      if request.method == "POST":
 
            miFormulario = UsuarioForm(request.POST)
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  usuario = Usuario(nombre=informacion["nombre"], email=informacion["email"])
                  usuario.save()
                  return render(request, "Home/base.html")
      else:
            miFormulario = UsuarioForm()
 
      return render(request, "usuario/crear.html", {"miFormulario": miFormulario})
