from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "Home/index.html")

def registro_view(request):
    if request.method == 'POST':
        # Procesar el formulario de registro
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Realizar las acciones necesarias, como crear un nuevo usuario en la base de datos
        
        # Redirigir al usuario a una página de éxito o a otra ubicación deseada
        
    return render(request, 'Home/base.html')