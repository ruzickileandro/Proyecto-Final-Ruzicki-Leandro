from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from usuario import views

app_name = "usuario"

urlpatterns = [
    path('crear_usuario/', views.crear_usuario, name='crear_usuario'),
    path('login/', views.login_request, name="login"),
    #path('logout/', views.logout_request, name='logout')
]

urlpatterns += staticfiles_urlpatterns()