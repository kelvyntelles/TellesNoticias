from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("noticia/<int:id>", views.noticia, name='noticia'),
    path("cidade/<int:id>", views.cidade, name='cidade'),
]
