from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Raça(models.Model):
    raça = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.raça


class Tag(models.Model):
    tag = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.tag

class novo_pet(models.Model):
    choices_status = (('P', 'Para adoção'),
                      ('A', 'Adotado'))

    username = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    foto = models.ImageField(upload_to="fotos_pets")
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    estado = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    telefone = models.CharField(max_length=50)
    tags = models.ManyToManyField(Tag)
    raca = models.ForeignKey(Raça, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=1, choices=choices_status, default='P')

    def __str__(self) -> str:
        return self.nome