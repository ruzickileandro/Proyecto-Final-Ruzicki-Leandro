from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views
from .views import home

app_name = "Home"

urlpatterns = [
    path("", home, name="home"),
    #path('registro/', views.registro_view, name='registro'),
]

urlpatterns += staticfiles_urlpatterns()