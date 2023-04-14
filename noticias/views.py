from django.shortcuts import render
from .models import Cidade, Noticia
from propagandas.models import PropagandaLateral, Banner, Colaboradores, BannerRotativo


def home(request):
    cidades = Cidade.objects.all()
    noticias = Noticia.objects.all()

    lista_noticias = list(reversed(noticias))
    banners = Banner.objects.all()
    colaboradores = Colaboradores.objects.all()
    banners_rotativos = BannerRotativo.objects.all()

    noticias_exibidas = []
    numero_noticias = 10
    iterador = 0

    if numero_noticias > len(lista_noticias):
        noticias_exibidas = lista_noticias
    else:
        while iterador < numero_noticias:
            noticias_exibidas.append(lista_noticias[iterador])
            iterador = iterador + 1

    propagandas_lateral = PropagandaLateral.objects.all()

    return render(request, 'home.html', {
        'cidades': cidades,
        'noticias': noticias_exibidas,
        'propagandas_lateral': propagandas_lateral,
        'banners': banners,
        'colaboradores': colaboradores,
        'banners_rotativos': banners_rotativos
    })


def noticia(request, id):
    cidades = Cidade.objects.all()
    noticia = Noticia.objects.get(id=id)

    fotos = noticia.fotos.all()

    propagandas_lateral = PropagandaLateral.objects.all()
    banners = Banner.objects.all()
    colaboradores = Colaboradores.objects.all()
    banners_rotativos = BannerRotativo.objects.all()

    return render(request, 'noticia.html', {
        'cidades': cidades,
        'noticia': noticia,
        'fotos': fotos,
        'propagandas_lateral': propagandas_lateral,
        'banners': banners,
        'colaboradores': colaboradores,
        'banners_rotativos': banners_rotativos
    })


def cidade(request, id):
    cidades = Cidade.objects.all()
    cidade = Cidade.objects.get(id=id)
    titulo = cidade.nome
    noticias = Noticia.objects.filter(cidade=id)
    lista_noticias = list(reversed(noticias))
    propagandas_lateral = PropagandaLateral.objects.all()
    banners = Banner.objects.all()
    colaboradores = Colaboradores.objects.all()
    banners_rotativos = BannerRotativo.objects.all()

    return render(request, 'home.html', {
        'cidades': cidades,
        'noticias': lista_noticias,
        'titulo': titulo,
        'propagandas_lateral': propagandas_lateral,
        'banners': banners,
        'colaboradores': colaboradores,
        'banners_rotativos': banners_rotativos
    })

