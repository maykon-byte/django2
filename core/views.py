from django.shortcuts import render
from . forms import contatoform
from django.contrib import messages

def index(request):
    return render(request,'index.html')


def contato(request):
    form=contatoform(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            nome= form.cleaned_data['nome']
            email= form.cleaned_data['email']
            assunto= form.cleaned_data['assunto']
            mensagem= form.cleaned_data['mensagem']

            print('mensagem enviada')
            print(f'nome: {nome}')
            print(f'email: {email}')
            print(f'assunto: {assunto}')
            print(f'mensagem: {mensagem}')

            messages.success(request,'email enviado com sucesso!')
            form=contatoform()
        else:
            messages.error(request,'erro ao enviar email!')
    context={
        'form':form
    }
    return render(request,'contato.html',context)


def produto(request):
    return render(request,'produto.html')

