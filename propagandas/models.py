from django.db import models


class PropagandaLateral(models.Model):
    titulo = models.CharField(max_length=100, default='foto')
    img = models.ImageField(upload_to='post_img')

    def __str__(self):
        return self.titulo


class Banner(models.Model):
    titulo = models.CharField(max_length=100, default='foto')
    img = models.ImageField(upload_to='post_img')

    def __str__(self):
        return self.titulo


class Colaboradores(models.Model):
    titulo = models.CharField(max_length=100, default='foto')
    img = models.ImageField(upload_to='post_img')

    def __str__(self):
        return self.titulo


class BannerRotativo(models.Model):
    titulo = models.CharField(max_length=100, default='foto')
    img = models.ImageField(upload_to='post_img')

    def __str__(self):
        return self.titulo