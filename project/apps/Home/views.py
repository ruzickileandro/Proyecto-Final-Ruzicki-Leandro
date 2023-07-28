from django.shortcuts import render
from apps.evento.models import Evento
# Create your views here.

def home_view(request):
    return render(request, "Home/base.html", {'eventos': Evento.objects.all().order_by('fecha')})

def registro_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
    return render(request, 'Home/base.html')