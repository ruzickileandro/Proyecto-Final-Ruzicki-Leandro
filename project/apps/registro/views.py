from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Registro
from apps.evento.models import Evento

@login_required
def registrar_interes(request, evento_id):
    if request.method == 'POST':
        evento = get_object_or_404(Evento, id=evento_id)
        usuario = request.user
        registro_existente = Registro.objects.filter(usuario=usuario, evento=evento).exists()
        if registro_existente:
            messages.warning(request, 'Ya te has interesado en este evento anteriormente.')
        else:
            registro = Registro(usuario=usuario, evento=evento)
            registro.save()
            messages.success(request, 'Gracias por interesarte en este evento.')
        return redirect('evento:detalle_evento', evento_id=evento_id)
    else:
        return redirect('usuario:login')