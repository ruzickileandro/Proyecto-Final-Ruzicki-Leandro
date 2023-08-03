from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

app_name = "usuario"

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_request, name="login"),
    path('logout/', LogoutView.as_view(template_name="usuario/logout.html"), name="logout"),
]

urlpatterns += staticfiles_urlpatterns()