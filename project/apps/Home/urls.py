from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
from django.urls import path
from . import views

app_name = "Home"

urlpatterns = [
    path("", views.home_view, name="home"),
    path('registro/', views.registro_view, name='registro'),
    path('about/', TemplateView.as_view(template_name="Home/about.html"), name="about"),
]

urlpatterns += staticfiles_urlpatterns()