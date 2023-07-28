from django.shortcuts import render
from . forms import contatoform

def index(request):
    return render(request,'index.html')


def contato(request):
    form=contatoform()
    context={
        'form':form
    }
    return render(request,'contato.html',context)


def produto(request):
    return render(request,'produto.html')

