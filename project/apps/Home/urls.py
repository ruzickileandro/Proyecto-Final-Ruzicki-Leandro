from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views

app_name = "Home"

urlpatterns = [
    path("", views.home_view, name="home"),
    path('registro/', views.registro_view, name='registro'),
]

urlpatterns += staticfiles_urlpatterns()