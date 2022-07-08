from django.urls import path
from .views import IndexView, TesteView

"""
Fazendo o import da class IndexView, que criamos em nossa view. E definindo para a rota raiz
do nosso projeto, ou seja, nossa página principal, eu irei executar a IndexView como uma função.
Por último estou dando um nome a url.
"""

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("teste/", TesteView.as_view(), name="teste"),
]
