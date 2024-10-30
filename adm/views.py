from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User, Permission
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from adm.forms import ProdutoForm
from .models import *
from django.core.paginator import Paginator
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . serializer import *
from rest_framework.parsers import MultiPartParser, FormParser


# Create your views here.

#Página de Erro
def error404(request, exception):
    return render(request, 'error404.html')

#Páginas web
# def main(request):
#     return render('')

def adm(request):
    context = {
        'page_title': 'Login'
    }
    return render(request, 'login.html', context)

def painelControle(request):
    context = {
        'page_title': 'Painel de Controle'
    }
    return render(request, 'painelControle.html', context)

def senha(request):
    context = {
        'page_title': 'Alterar Senha'
    }
    return render(request, 'alterarsenha.html', context)

def inicio(request):
    context = {
        'page_title': 'Início'
    }
    return render(request, 'inicio.html', context)

def produtos(request):
    data = {}
    
    buscar = request.GET.get('search')
    if buscar:
        # Usando Q para combinar múltiplos filtros
        data['db'] = Produtos.objects.filter(
            Q(nome__icontains=buscar) |
            Q(descricao__icontains=buscar) |
            Q(peso__icontains=buscar) |
            Q(preco__icontains=buscar)
        )
    else:
        data['db'] = Produtos.objects.all()
    
    # Paginação
    all = data['db']  # Usar o conjunto de resultados filtrados
    paginator = Paginator(all, 8)
    pages = request.GET.get('page')
    
    data['page_title'] = 'Produtos'
    data['db'] = paginator.get_page(pages)
    
    return render(request, 'produtos.html', data)


def usuarios(request):
    data = {}
    
    
    all = User.objects.all()
    paginator = Paginator(all, 10)
    pages = request.GET.get('page')
    
    data = {
        'db': paginator.get_page(pages),
        'page_title': 'Usuários'
    }
    return render(request, 'usuarios.html', data)

def dashboard_produtos(request):
    context = {
        'page_title': 'Dashboard de Produtos'
    }
    return render(request, 'dashboard_produtos.html', context)

def dashboard_balanco(request):
    context = {
        'page_title': 'Dashboard do Balanço'
    }
    return render(request, 'dashboard_balanco.html', context)

def createprodutos(request):
    data = {
        'page_title': 'Criar Produtos',
        'forms': ProdutoForm()
    }
    return render(request, 'produtos_forms.html', data)

#***Funções ações e etc***

#cadastrar usuário no sistema
def CadastroUsuario(request):
    data = {}
    if(request.POST['senha'] != request.POST['confirmasenha']):
        data['msg'] = 'Senha e confirmação de senha diferentes!'
        data['class'] = 'alert-danger'
    else:
        user = User.objects.create_user(
            request.POST['usuario'], 
            request.POST['usuario'], 
            request.POST['senha'])
        user.first_name = request.POST['nome']
        user.save()
        data['msg'] = 'Usuário Cadastrado com Sucesso'
        data['class'] = 'alert-success'
    return render(request, 'login.html', data)

#rota de login, valida os dados do usuário e acessa os serviços
def logar(request):
    data = {}
    user = authenticate(
        username=request.POST['emaillogin'], 
        password=request.POST['senhalogin'])
    
    if user is not None:
        login (request, user)
        return redirect ('/painelcontrole/')
    else:
        data['msg'] = 'Usuário ou Senha inválidos!'
        data['class'] = 'alert-danger'
        return render(request, 'login.html', data)

#rota para sair do login
def logauts(request):
    logout(request)
    return redirect ('/')

#rota para alterar senhha
def alterarsenha(request):
    data = {}
    user = User.objects.get(username=request.user.email)
    user.set_password(request.POST['password'])
    if (request.POST['password'] != ""):
        user.save()
        data['msg'] = 'Senha Alterada com Sucesso!'
        data['class'] = 'alert-success'
        logout(request)
        return render(request, 'login.html', data)
    else:
        data['msg'] = 'Campo Senha Vazio!'
        data['class'] = 'alert-danger'
        return render(request, 'alterarSenha.html', data)
    
    

def edit_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    perms = Permission.objects.all()
    
    # Recupera as permissões do usuário como um queryset
    user_permissions = user.user_permissions.all()  

    if request.method == 'POST':
        user.first_name = request.POST.get('nome')
        user.email = request.POST.get('email')
        user.is_active = request.POST.get('status') == 'True'

        # Adicionar permissão
        add_permissao = request.POST.get('add_permissao')
        if add_permissao:
            try:
                permission = Permission.objects.get(name=add_permissao)
                user.user_permissions.add(permission)
            except Permission.DoesNotExist:
                pass  # ou exibir mensagem de erro

        # Remover permissões
        remover_permissoes = request.POST.get('remover_permissoes').split(',')
        for perm_name in remover_permissoes:
            perm_name = perm_name.strip()  # Remover espaços em branco
            if perm_name:
                try:
                    permission = Permission.objects.get(codename=perm_name)  # Aqui procura pelo codename
                    user.user_permissions.remove(permission)
                except Permission.DoesNotExist:
                    pass  # ou exibir mensagem de erro

        user.save()
        return redirect('edit_user', pk=pk)

    data = {
        'db': user,
        'perms': perms,
        'user_permissions': user_permissions,  # Passando o queryset de permissões do usuário
        'page_title': 'Editar Usuário'
    }

    return render(request, 'edit_user.html', data)

def AdicionarProduto(request):
    data = {}
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            data['msg'] = 'Produto cadastrado com sucesso!'
            data['class'] = 'alert-success'
            return redirect('Criar Produto')
            
        else:
            data['msg'] = 'Erro ao cadastrar o produto. Verifique os dados.'
            data['class'] = 'alert-danger'
    else:
        form = ProdutoForm()
    
    
    data['forms'] = form  # Adiciona o formulário ao dicionário de dados
    
    return render(request, 'produtos.html', data)

def edit_produtos(request, pk):
    data = {}
    data['db'] = Produtos.objects.get(pk=pk)
    data['forms'] = ProdutoForm(instance=data['db'])
    return render(request, 'produtos_forms.html', data)
    
    

def update_produtos(request, pk):
    data = {}
    data['db'] = Produtos.objects.get(pk=pk)
    form = ProdutoForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('produtos')

def delete_produtos(request, pk):
    db = Produtos.objects.get(pk=pk)
    db.delete()
    return redirect('produtos')




#*** FrontEnd REACT ***
class ReactViewProd(APIView):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = ReactSerializerProdutos
    def get(self, request):
        produtos = Produtos.objects.all()
        serializer = ReactSerializerProdutos(produtos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReactSerializerProdutos(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

# class ReactViewProd(APIView):
    
#     serializer_class = ReactSerializerProdutos
    
#     def get(self, request):
#         output = [
#             {
#                 'nome': output.nome, 
#                 'descricao': output.descricao, 
#                 'preco': output.preco, 
#                 'peso': output.peso, 
#                 'imagem': output.imagem, 
#                 'status': output.status, 
#                 'data_adicionado': output.data_adicionado,
#             }
#             for output in Produtos.objects.all()
#         ]
#         return Response(output)
#     def post(self, request):
#         serializer = ReactSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)

class ReactView(APIView):
    
    serializer_class = ReactSerializer
    
    def get(self, request):
        output = [{
                "employee": output.employee, 
                "departament": output.departament}
                for output in React.objects.all()]
        return Response(output)
    
    def post(self, request):
        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

# class main(APIView):
#     def casa(request):
#         return response()

def main(request):
    return redirect('adm/')