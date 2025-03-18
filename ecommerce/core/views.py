from django.http import HttpResponse
from django.shortcuts import render
from produtos.models import Produto

def buscar(request):
    query = request.GET.get('pesquisa')
    if query:
        produtos = Produto.objects.filter(nome__icontains=query)
    else:
        produtos = Produto.objects.all()
    return render(request, 'busca_produto.html', {'produtos': produtos, 'query': query})

def para_sua_empresa(request):
    return render(request, 'para_sua_empresa.html')

def baixe_o_app(request):
    return render(request, 'baixe_o_app.html')

def receba_hoje(request):
    return render(request, 'receba_hoje.html')

def cartao_de_credito(request):
    return render(request, 'cartao_de_credito.html')

def marcas_proprias(request):
    return render(request, 'marcas_proprias.html')

def produtos_internacionais(request):
    return render(request, 'produtos_internacionais.html')

def venda_na_ecommerce(request):
    return render(request, 'venda_na_ecommerce.html')

def oferta(request):
    return render(request, 'oferta.html')