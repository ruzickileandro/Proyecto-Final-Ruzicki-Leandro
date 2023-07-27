from django import forms
from apps.evento.models import Evento, EventoCategoria
from django.shortcuts import render

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['titulo', 'descripcion', 'fecha', 'categoria']

    categoria = forms.ModelChoiceField(queryset=EventoCategoria.objects.all())

def eventoFormulario(request):
 
      if request.method == "POST":
 
            miFormulario = EventoForm(request.POST)
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  usuario = Evento(titulo=informacion["titulo"],
                                   descripcion=informacion["descripcion"],
                                   fecha=informacion["fecha"],
                                   categoria=informacion["categoria"])
                  usuario.save()
                  return render(request, "Home/base.html")
      else:
            miFormulario = EventoForm()
 
      return render(request, "evento/crear_evento.html", {"miFormulario": miFormulario})