import uuid
from distutils.command.upload import upload
from django.db import models
from stdimage.models import StdImageField


def get_file_path(_instance, filename):
    """
    ext --> Recebemos uma string, então daremos um split no ponto da string (nome do arquivo que vamos receber)
    Vamos pegar a extensão do arquivo, em seguida estamos colocando o nome do arquivo em filename e gerando um nome aleatório
    concatenando com a extensão que pegamos anteriormente. Para usarmos, vamos lá onde estamos fazendo upload da imagem
    e em upload_to, vamos passar o get_file_path. --> upload_to=get_file_path
    """
    ext = filename.split(".")[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return filename


class Base(models.Model):
    criados = models.DateField("Criação", auto_now_add=True)
    """
    auto_now_add, vai automaticamente adicionar a data assim que o nosso
    objeto for criado
    """
    modificado = models.DateField("Atualização", auto_now=True)
    """
    A diferença de auto_now_add e auto_now, é que o add, vai colocar esse
    valor somente na adição, ou seja, quando o novo objeto for criado. Já o auto now
    toda vez que o objeto for modificado, o valor vai ser automaticamente atualizado. 
    """
    ativo = models.BooleanField("Ativo ?", default=True)

    class Meta:
        abstract = True


class Servico(Base):
    icone_choices = (
        ("lni-cog", "Engrenagem"),
        ("lni-stats-up", "Gráfico"),
        ("lni-users", "Usuários"),
        ("lni-layers", "Design"),
        ("lni-mobile", "Mobile"),
        ("lni-rocket", "Foguete"),
    )
    """
    icone_choices --> Para nós cadastrarmos um serviço, note que precisamos informar qual ícone
    que a pessoa cadastrada vai utilizar. Passamos o mesmo nome dos ícones, que temos em nosso template em seguida
    estamos passando uma éspecie de tradução, para ficar mais fácil. Ex.: lni-rocket mostra um ícone de foguete.
    """
    servico = models.CharField("Serviços", max_length=100)
    descricao = models.TextField("Descrição", max_length=200)
    icone = models.CharField("ícone", max_length=12, choices=icone_choices)
    """
    Note que o nosso campo icone_choices, é na verdade uma tupla. No campo icone, estamos passando um charfield
    que irá receber no máximo 12 caracteres (que é o ícone com maior quantidade de caracteres que temos em nossa tupla)
    e em seguida estamos passando o choices e colocando como valor a nossa tupla. Ou seja, o campo CharField, vai receber
    um valor entre os itens da nossa tupla icone_choices. O usuário vai escolher algum desses ícones, na hora de cadastrar o serviço.
    """

    class Meta:
        """
        Lembre que em programação nós não utilizamos acentuação, cedilha. Em nosso área administrativa não queremos
        apresentar o nome da nossa class do jeito que está aqui (Servico). Para isso criamos a class Meta, com as variáveis
        verbosa_name = serviços (o nome de apresentação), e o verbosa_name_plural que vai apresentar a nossa class no plural.
        """

        verbose_name = "Serviço"
        verbose_name_plural = "Serviços"

    def __str__(self):
        """
        Está função nos permite apresentar os dados cadastrados em nossa área administrativa. Retorna uma string
        dos nossos campos.
        """
        return self.servico
        """
        Estamos passando o nosso campo servico.
        """


class Cargo(Base):
    cargo = models.CharField("Cargo", max_length=100)

    class Meta:
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"

    def __str__(self):
        return self.cargo


class Funcionario(Base):
    nome = models.CharField("Nome", max_length=100)
    cargo = models.ForeignKey(
        "core.Cargo", verbose_name="cargo", on_delete=models.CASCADE
    )
    """
    Note que estamos dizendo que cargo é uma chave estrangeira. Vamos pegar o valor do campo cargo da nossa class Cargo e passar 
    no campo cargo da class Equipe.
    Sempre que lidamos com chave estrangeira no django, precisamos passar o on_delete=models.CASCADE --> Imagine que
    temos um funcionário que é programador, caso o cargo de programador seja excluido, se este cargo for excluido, o funcionário
    cadastrado com o cargo de programador também será excluido.
    """
    bio = models.TextField("Bio", max_length=100)
    image = StdImageField(
        "Imagem",
        upload_to=get_file_path,
        variations={"thumb": {"width": 480, "height": 480, "crop": True}},
    )
    """
    Isto vai criar um diretório media e criar um diretório Equipe dentro de media, onde será armazenada as imagens. Variations
    vai colocar as imagens na proporção 480 x 480 como definimos e crop irá cortar a imagem, caso seja preciso.
    480 x 480 é o tamanho que o nosso template pode receber na div. Caso a imagem que nós enviarmos através do cadastro for maior, será 
    criado uma variação em 480x480.
    """
    facebook = models.CharField("Facebook", max_length=100, default="#")
    instagram = models.CharField("Instagram", max_length=100, default="#")
    twitter = models.CharField("Twitter", max_length=100, default="#")
    """
    Passando a rede social dos nossos funcionários. Caso o campo fique vazio, o valor será --> #
    """

    class Meta:
        verbose_name = "Funcionário"
        verbose_name_plural = "Funcionários"

    def __str__(self):
        return self.nome


class Features(Base):
    icone_choices = (
        ("lni-cog", "Engrenagem"),
        ("lni-stats-up", "Gráfico"),
        ("lni-users", "Usuários"),
        ("lni-layers", "Design"),
        ("lni-mobile", "Mobile"),
        ("lni-rocket", "Foguete"),
    )
    icone = models.CharField("icone", max_length=12, choices=icone_choices)
    nome = models.CharField("Nome", max_length=100)
    texto = models.TextField("Texto", max_length=200)

    class meta:
        verbose_name = "Feature"
        verbose_name_plural = "Features"

    def __str__(self):
        return self.nome


