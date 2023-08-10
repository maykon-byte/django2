from django import forms
from django.core.mail.message import EmailMessage

class contatoform(forms.Form):
    nome= forms.CharField(label='nome',max_length=100)
    email= forms.EmailField(label='email',max_length=100)
    assunto=forms.CharField(label='assunto',max_length=120)
    mensagem=forms.CharField(label='mensagem',widget=forms.Textarea())


# def send_mail(self):
#     nome=self.cleaned_data['nome']
#     email=self.cleaned_data['email']
#     assunto=self.cleaned_data['assunto']
#     mensagem=self.cleaned_data['mensagem']

#     conteudo=f'nome: {nome}\nemail: {email}\nassunto: {assunto}\nmensagem: {mensagem}'

#     mail=EmailMessage(
#         subject='email enviado pelo sistema django2',
#         body=conteudo,
#         from_email='contato@seudominio.com.br',
#         to=['contato@seudominio.com.br',],
#         headers={'reply-to': email}
#     )
#     mail.send()