from django.shortcuts import render
from .models import Usuario
# Create your views here.


def home(request):
    return render(request, 'usuarios/home.html')

def cadastro_usuario(request):
    #salvar dados da entrada para o banco de dados
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()
    #exibir ja cadastrados
    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    #Retorno de dados
    return render(request, 'usuarios/usuarios.html', usuarios)