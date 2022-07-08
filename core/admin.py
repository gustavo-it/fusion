from django.contrib import admin
from .models import Cargo, Servico, Funcionario, Features


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ("cargo", "ativo", "modificado")
    """
    Passando aqui o nome dos nossos campos que serão exibidos na área administrativa.
    Lembrando que os nossos campos não possuem acentuação.
    modificado e ativo são referentes aos campos que criamos em nossa class Base. Como cargo
    herda de Base, ele também terá esses campos.
    O decorator admin.register --> Utilizamos para registrar o nosso produto.
    """


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ("servico", "icone", "ativo", "modificado")


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ("nome", "cargo", "ativo", "modificado")


@admin.register(Features)
class FeaturesAdmin(admin.ModelAdmin):
    list_display = ("nome", "icone", "texto", "modificado", "ativo")
