from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.urls import reverse_lazy
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
    
@login_required(login_url=reverse_lazy('usuario:login'))
def quitar_interes(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    registro = Registro.objects.filter(evento=evento, usuario=request.user).first()
    if registro:
        registro.delete()
        messages.success(request, 'Te desuscribiste de este evento.')
    return redirect('evento:detalle_evento', evento_id=evento_id)

def lista_usuarios_eventos(request):
    registros = Registro.objects.select_related('usuario', 'evento').all()

    usuarios_intereses = {}
    for registro in registros:
        usuario = registro.usuario
        evento = registro.evento

        if usuario not in usuarios_intereses:
            usuarios_intereses[usuario] = []
        
        usuarios_intereses[usuario].append(evento)

    return render(request, 'registro/lista_usuarios_eventos.html', {'usuarios_intereses': usuarios_intereses})

@staff_member_required
def eliminar_registro(request, usuario_id, evento_id):
    registro = get_object_or_404(Registro, usuario_id=usuario_id, evento_id=evento_id)

    if request.method == 'POST':
        registro.delete()
        messages.success(request, 'Registro eliminado correctamente.')
    return redirect('registro:lista_usuarios_eventos')