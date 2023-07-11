from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "Home/index.html")

def registro_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
    return render(request, 'Home/base.html')