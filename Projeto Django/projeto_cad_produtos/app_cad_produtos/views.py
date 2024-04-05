from django.shortcuts import render
from .models import Produto

def home(request):
    return render(request, 'produtos/home.html')

def produtos(request): 
    
    #salva os dados da tela no banco de dados
    novo_produto = Produto()
    novo_produto.nome = request.POST.get('nome')
    novo_produto.marca = request.POST.get('marca')
    novo_produto.quantidade = request.POST.get('quantidade')
    novo_produto.save()
    #exibe todos os itens ja cadastrados em uma nova pagina
    
    produtos = {
        'produtos': Produto.objects.all()
    }
    #RETORNA OS DADOS PARA A PAGINA DE LISTAGEM DE PRODUTOS
    return render (request,'produtos/produtos.html', produtos)

