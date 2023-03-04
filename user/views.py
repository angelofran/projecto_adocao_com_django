from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth import authenticate, login, logout


# Cadastrar
def register(request):
    if request.user.is_authenticated:
        return redirect('/divulgar/novo_pet')
    if request.method == "GET":
        return render(request, 'register.html')
    else:
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        senha_confirm = request.POST.get('confirmar_senha')
        if len(nome.strip()) == 0 or len(email.strip()) == 0 or len(senha.strip()) == 0 or len(senha_confirm.strip()) == 0:
            messages.add_message(request, constants.ERROR, "Complete os espaços.")
            return render(request, 'register.html')
            
        if senha != senha_confirm:
            messages.add_message(request, constants.ERROR, "As senhas não coincidem.")
            return render(request, 'register.html')

        try:
            user = User.objects.create_user(
                username=nome,
                email=email,
                password=senha,
            )
            return redirect('/user/login/')
        except Exception as err:
            print(err)
            messages.add_message(request, constants.ERROR, "Erro Interno")
            return render(request, 'register.html')


#login
def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        user = authenticate(username=nome, password=senha)
        if user is not None:
            login(request)
            return redirect('/divulgar/novo_pet')
        else:
            messages.add_message(request, constants.ERROR, 'Usuário ou senha inválidos')
            return render(request, 'login.html')

def sair(request):
    logout(request)
    return redirect('/user/login/')
