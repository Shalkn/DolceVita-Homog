from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User, Permission
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

# Create your views here.

#Páginas web
def main(request):
    return redirect('/adm/')

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
    context = {
        'page_title': 'Produtos'
    }
    return render(request, 'produtos.html', context)


def usuarios(request):
    
    data = {
        'db': User.objects.all(),
        'page_title': 'Usuários'
    }

    return render(request, 'usuarios.html', data)

# def edit_user(request, pk):
    
#     user = get_object_or_404(User, id=pk)
#     if request.method == 'POST':
#         form = UserChangeForm(request.POST, instance=user)
#         if form.is_valid():
#             form.save()
#             return redirect('editar_usuario', user_id=user.id)
#     else:
#         form = UserChangeForm(instance=user)
    
#     data = {
#         'db': form,
#         'db': user,
#         'perms': Permission.objects.all(),
#         'page_title': 'Editar Usuário',
        
#     }
#     return render(request, 'edit_user.html', data)



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

#Funções ações e etc

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