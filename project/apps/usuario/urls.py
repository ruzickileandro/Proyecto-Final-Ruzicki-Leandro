from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from .views import crear_usuario
from apps.Home.views import home
from usuario import views

app_name = "usuario"

urlpatterns = [
    path('', include("Home.urls")),
    path('', home, name='home'),
    path('crear_usuario/', crear_usuario, name='crear_usuario'),
    path('login/', views.login_request, name="login"),
    
]

urlpatterns += staticfiles_urlpatterns()