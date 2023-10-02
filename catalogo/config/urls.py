"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('ator/', ator, name='ator'),
    path('categoria/', categoria, name='categoria'),
    path('continente/', continente, name='continente'),
    path('diretor/', diretor, name='diretor'),
    path('episodio/', episodio, name='episodio'),
    path('filme_ator/', filme_ator, name='filme_ator'),
    path('filme/', filme, name='filme'),
    path('nacionalidade/', nacionalidade, name='nacionalidade'),
    path('pais/', pais, name='pais'),
    path('serie_episodio/', serie_episodio, name='serie_episodio'),
    path('serie/', serie, name='serie'),
    path('temporada/', temporada, name='temporada'),
]
