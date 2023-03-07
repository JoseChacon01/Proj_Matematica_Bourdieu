from django.shortcuts import redirect, render
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login # as duas funções responsáveis pela autenticação: 1-authenticate - verifica o login e senha; 2- login - realiza a autenticação no sistema.
from django.contrib.auth import logout #função responsável pelo logout
from django.contrib.auth.decorators import permission_required #Definindo que o acesso à View só será feito por usuários que tiverem a permissão permissao_adm_1 definida:
from django.contrib.auth.models import Permission #Primeiro passo: Importar o objeto Permission em Views:
from django.contrib.auth.forms import UserCreationForm #Registro: UserCreationForm: é um ModelForm que já vem implementado no Django, com 3 campos para o registro de usuário: username, password1 e password2.
from .forms import  CategoriaForm #importando a class criado em forms.py 
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Categoria, Usuario

def home (resquest):
    return render(resquest, "index.html")

def cadastro(resquest):
    return render(resquest, "cadstro.html")

def noticias(resquest):
    return render(resquest, "noticias.html") 

@login_required
def perfil (resquest):
    return render(resquest, "perfil.html")




def autenticacao(request): 
    if request.POST: 
        username = request.POST['usuario']
        password = request.POST['senha']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('perfil')
        else:
            return render(request, 'registration\login.html')
    else:
        return render(request, 'registration\login.html')


def desconectar(request):
    logout(request)
    return redirect('home')





def cadastro_manual(request):
    user = Usuario.objects.create_user(
        username='admin',
        email='admin@email.com',
        cpf='11111111111',
        nome='Administrador',
        password='admin12345',
        idade=30,
        is_superuser=False)
    user.save()
    return redirect('home')





#Categoria

def listar_categoria(request):       
    categoria = Categoria.objects.all()
    contexto = {
        'todas_categoria': categoria
    }
    return render (request, 'categoria.html', contexto)


def cadastrar_categoria(request):     
    form = CategoriaForm(request.POST or None)

    if form.is_valid(): 
        form.save()
        return redirect('listar_categoria') 

    contexto = {
        'form_categoria': form
    }
    return render(request, 'categoria_cadastrar.html', contexto)



def editar_categoria(request, id): #EDITAR nome da categoria
    categoria = Categoria.objects.get(pk=id)

    form = CategoriaForm(request.POST or None, instance=categoria)

    if form.is_valid():
        form.save()
        return redirect('listar_categoria')

    contexto = {
        'form_categoria': form
    }    

    return render (request, 'categoria_cadastrar.html', contexto)



def remover_categoria(request, id): 
    categoria = Categoria.objects.get(pk=id) 
    categoria.delete()
    return redirect('listar_categoria') 
