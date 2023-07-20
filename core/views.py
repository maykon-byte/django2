from django.shortcuts import render

def index(request):
    return(request,'index.html')


def contato(request):
    return(request,'contato.html')


def produto(request):
    return(request,'produto.html')

