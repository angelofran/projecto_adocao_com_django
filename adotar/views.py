from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from divulgar.models import novo_pet, Raça
# Create your views here.

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

