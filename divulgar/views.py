from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.contrib import messages
from django.contrib.messages import constants
from .models import Tag, Raça, novo_pet
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def new_pet(request):
    if request.method == "POST":
        foto = request.FILES.get('foto')
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        estado = request.POST.get('estado')
        cidade = request.POST.get('cidade')
        telefone = request.POST.get('telefone')
        tags = request.POST.getlist('tags')
        raca = request.POST.get('raca')

        pet = novo_pet(username=request.user, foto=foto, nome=nome, descricao=descricao, estado=estado, cidade=cidade, telefone=telefone, raca_id=raca)
        pet.save() 

        for tag_id in tags:
            tag = Tag.objects.get(id=tag_id)
            pet.tags.add(tag)
            
        pet.save()     

        tags = Tag.objects.all()
        racas = Raça.objects.all()       

        messages.add_message(request, constants.SUCCESS, 'Novo pet cadastrado')
        return redirect('/divulgar/seus_pets') 

    elif request.method == "GET":
        tags = Tag.objects.all()
        racas = Raça.objects.all()
        return render(request, 'newpet.html', {'tags' : tags, 'racas' : racas})

    else:
        messages.add_message(request, constants.ERROR, "Erro Interno")
        return render(request, 'newpet.html')


@login_required
def seus_pets(request):
    if request.method == "GET":
        pets = novo_pet.objects.filter(username=request.user)
        return render(request, 'seus_pets.html', {'pets': pets})


@login_required
def remover_pets(request, id):
    pet = novo_pet.objects.get(id=id)
    if not pet.username == request.user:
        messages.add_message(request, constants.ERROR, "Esse pet não é seu.(expertinho)")
        return redirect('/divulgar/seus_pets')

    pet.delete()
    messages.add_message(request, constants.SUCCESS, "Removido com sucesso")
    return redirect('/divulgar/seus_pets')
    
@login_required
def ver_pet(request , id):
    if request.method == "GET":
        pet = novo_pet.objects.get(id=id)
        return render(request, 'ver_pet.html', {'pet':pet})