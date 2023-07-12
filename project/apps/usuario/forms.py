from django import forms
from apps.usuario.models import Usuario
from django.shortcuts import render

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'email', 'contraseña']

def usuarioFormulario(request):
 
      if request.method == "POST":
 
            miFormulario = UsuarioForm(request.POST)
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  usuario = Usuario(nombre=informacion["nombre"],
                                   apellido=informacion["apellido"],
                                   email=informacion["email"],
                                   contraseña=informacion["contraseña"])
                  usuario.save()
                  return render(request, "Home/base.html")
      else:
            miFormulario = UsuarioForm()
 
      return render(request, "usuario/crear_usuario.html", {"miFormulario": miFormulario})
