from django import forms
# importando a class forms
from django.core.mail.message import EmailMessage

# Configurando nosso servidor de email


class ContatoForm(forms.Form):
    """
    Criando os campos do nosso formulár
    Widget Textarea() --> Vai exibir nosso Charfield como um textarea, um campo maior.
    """

    nome = forms.CharField(label="Nome", max_length=100)
    email = forms.EmailField(label="E-mail", max_length=100)
    assunto = forms.CharField(label="Assunto", max_length=100)
    mensagem = forms.CharField(label="Mensagem", widget=forms.Textarea())

    def send_mail(self):
        """
        Pegando os valores dos campos depois de preenchidos
        """
        nome = self.cleaned_data["nome"]
        email = self.cleaned_data["email"]
        assunto = self.cleaned_data["assunto"]
        mensagem = self.cleaned_data["mensagem"]

        conteudo = (
            f"Nome: {nome}\nE-mail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}"
        )
        """
        Vamos criar uma variável conteudo onde receberá os dados que o usuário colocou
        Vamos enviar um email com as informações, onde:
        subject --> É o assunto do email
        body --> É o corpo do email
        from_email --> por quem está sendo enviado esse email 
        to --> esse email será enviado para os endereços passando dentro da lista
        headers --> Para quem vou enviar a resposta do email.
        Por último estou enviando o email com --> mail.send()
        """
        mail = EmailMessage(
            subject=assunto,
            body=conteudo,
            from_email="contato@fusion.com.br",
            to=[
                "contato@fusion.com.br",
            ],
            headers={"Reply-To": email},
        )
        mail.send()
