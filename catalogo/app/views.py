from django.shortcuts import render
from . models import *

# Create your views here.

def categoria(request):
    
    consultas = {
        'consultas':Categoria.objects.all()
    }

    return render(request, 'consulta/categoria.html', consultas)

def episodio(request):
    
    consultas = {
        'consultas':Episodio.objects.all()
    }

    return render(request, 'consulta/episodio.html', consultas)

def nacionalidade(request):
    
    consultas = {
        'consultas':Nacionalidade.objects.all()
    }

    return render(request, 'consulta/nacionalidade.html', consultas)

def ator(request):
    
    consultas = {
        'consultas':Ator.objects.all()
    }

    return render(request, 'consulta/ator.html', consultas)

def diretor(request):
    
    consultas = {
        'consultas':Diretor.objects.all()
    }

    return render(request, 'consulta/diretor.html', consultas)

def temporada(request):
    
    consultas = {
        'consultas':Temporada.objects.all()
    }

    return render(request, 'consulta/temporada.html', consultas)

def continente(request):
    
    consultas = {
        'consultas':Continente.objects.all()
    }

    return render(request, 'consulta/continente.html', consultas)

def pais(request):
    
    consultas = {
        'consultas':Pais.objects.all()
    }

    return render(request, 'consulta/pais.html', consultas)

def filme(request):
    
    consultas = {
        'consultas':Filme.objects.all()
    }

    return render(request, 'consulta/filme.html', consultas)

def filme_ator(request):
    
    consultas = {
        'consultas':FilmeAtor.objects.all()
    }

    return render(request, 'consulta/filme_ator.html', consultas)

def serie(request):
    
    consultas = {
        'consultas':Serie.objects.all()
    }

    return render(request, 'consulta/serie.html', consultas)

def serie_episodio(request):
    
    consultas = {
        'consultas':SerieEpisodio.objects.all()
    }

    return render(request, 'consulta/serie_episodio.html', consultas)