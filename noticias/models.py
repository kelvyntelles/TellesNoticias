from django.db import models
from datetime import datetime


class Cidade(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Foto(models.Model):
    titulo = models.CharField(max_length=100, default='foto')
    img = models.ImageField(upload_to='post_img')

    def __str__(self):
        return self.titulo


class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    imgCapa = models.ImageField(upload_to='post_img')
    texto = models.TextField()
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    date_publicacao = models.DateField(default=datetime.now())
    fotos = models.ManyToManyField(Foto, related_name="noticias")

    def __str__(self):
        return self.titulo





