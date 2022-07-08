# from msilib.schema import Feature
from audioop import reverse
from multiprocessing import context
from django.urls import reverse_lazy
from django.views.generic import FormView

from core.forms import ContatoForm

"""
Para utilizarmos o template view, basta informarmos o nome do template com a variável
template_name.
Então criei uma class chamada IndexView que herda de TemplateView e estou passando o nome
do meu template.
Agora vamos mudar de TemplateView para FormView, pois estamos trabalhando com formulario.
Basta dizer que as nossas classes herdam de FormView
"""
from .models import Servico, Funcionario, Features

"""
Importando os models que queremos apresentar
"""
from .forms import ContatoForm

from django.urls import reverse_lazy

# Utilizado para redirecionar o usuário para uma página após enviar o formulário

from django.contrib import messages

# utilizado para exibir uma mensagem de sucesso ou erro, no momento de envio do formulario


class IndexView(FormView):
    """
    Estou dizendo que tenho uma página web que possui um formulário. O meu template continua sendo o index
    indicando a class do formulario, e no sucesso, se o formulário for válido, estou mandando o usuário de volta
    para o index.
    """
    template_name = "index.html"
    form_class = ContatoForm
    success_url = reverse_lazy("index")

    def get_context_data(self, **kwargs):
        """
        Estamos recuperando o contexto da página com esta função, ou seja, se já tem dados na página
        vindo de algum lugar, estamos pegando esse contexto.
        Mas também queremos adicionar no contexto da nossa página os serviços e funcionários.
        """
        context = super(IndexView, self).get_context_data(**kwargs)
        context["servicos"] = Servico.objects.order_by("?").all()
        """
        Pegando todos os objetos do nosso banco de dados com objects.all()
        Agora que temos os dados, vamos iterar sobre os objetos.
        """
        context["funcionarios"] = Funcionario.objects.filter(ativo=True)
        """
        Essas chaves (funcionario, servicos) utilizaremos para iterar sobre os objetos em nosso template.
        """
        context["features"] = Features.objects.filter(ativo=True)
        return context

    def form_valid(self, form, *args, **kwargs):
        """
        Se o formulário for valido vamos enviar o email, chamando a função criada lá em 
        forms.py
        O envio será feito com form.sed_mail(). Além disso estamos colocando uma mensagem de sucesso
        e retornar o formulário.
        """
        form.send_mail()
        messages.success(self.request, "E-mail enviado com sucesso !")
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        """
        Se o formulário não for válido, nós vamos exibir uma mensaggem de erro e retornar o formulário.
        """
        messages.erros(self.request, "Erro ao enviar o E-mail !")
        return super(IndexView, self).form_invalid(form, *args, **kwargs)


class TesteView(FormView):
    template_name = "500.html"
