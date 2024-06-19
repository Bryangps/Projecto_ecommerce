from django.shortcuts import render

# Create your views here.


def homepage(request):
    return render(request, 'loja/pages/homepage.html')


def loja(request):
    return render(request, 'loja/pages/loja.html')


def carrinho(request):
    return render(request, 'loja/pages/carrinho.html')


def checkout(request):
    return render(request, 'loja/pages/checkout.html')


def minha_conta(request):
    return render(request, 'loja/pages/minha_conta.html')


def login(request):
    return render(request, 'loja/pages/login.html')

