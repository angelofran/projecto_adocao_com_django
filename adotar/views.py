from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from divulgar.models import novo_pet, Raça
from .models import PedidoAdocao
from django.conf import settings
from django.contrib import messages
from django.contrib.messages import constants
from datetime import datetime
from django.core.mail import send_mail

@login_required
def listar_pets(request):
    if request.method == "GET":
        pets = novo_pet.objects.filter(status="P")
        racas = Raça.objects.all()

        cidade = request.GET.get('cidade')
        raca_filter = request.GET.get('raca')
        
        if cidade:
            pets = pets.filter(cidade__icontains=   cidade)
            
        if raca_filter:
            pets = pets.filter(raca__id=raca_filter)

        return render(request, 'index.html', {'pets':pets, 'racas':racas, 'cidade':cidade, 'racas_filter':raca_filter})

def pedido_adocao(request, id_pet):
    pet = novo_pet.objects.filter(id=id_pet).filter(status="P")

    if not pet.exists():
        messages.add_message(request, constants.ERROR, 'Esse pet já foi adotado :)')
        return redirect('/adotar')
    else:
 
        pedido = PedidoAdocao(pet=pet.first(),
                            usuario=request.user,
                            data=datetime.now())

        pedido.save()

        messages.add_message(request, constants.SUCCESS, 'Pedido de adoção realizado, você receberá um e-mail caso ele seja aprovado.')
        return redirect('/adotar')
    

def processa_pedido_adocao(request, id_pedido):
    status = request.GET.get('status')
    pedido = PedidoAdocao.objects.get(id=id_pedido)
    if status == "A":
        pedido.status = 'AP'
        string = '''Olá, sua adoção foi aprovada. ...'''
    elif status == "R":
        string = '''Olá, sua adoção foi recusada. ...'''
        pedido.status = 'R'

    pedido.save()

    
    print(pedido.usuario.email)
    email = send_mail(
        'Sua adoção foi processada',
        string,
        'caio@pythonando.com.br',
        [pedido.usuario.email,],
    )
    
    messages.add_message(request, constants.SUCCESS, 'Pedido de adoção processado com sucesso')
    return redirect('/divulgar/ver_pedido_adocao')