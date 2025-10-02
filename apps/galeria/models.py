from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Represeta tabela no banco de dados
class Fotografia(models.Model):

    OPCOES_CATEGORIA = [
        ("ASTROS","Astros"),
        ("MÚSICA","Música"),
        ("NATUREZA","Natureza"),
        ("ESPORTES","Esportes"),
        ("ANIMAIS","Animais"),
        ("CIDADES","Cidades"),
        ("PESSOAS","Pessoas"),
        ("TECNOLOGIA","Tecnologia"),
        ("OUTROS","Outros"),
    ]
        
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=50, choices=OPCOES_CATEGORIA ,default="")
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/", blank=True)
    publicada = models.BooleanField(default=True)
    data_fotografia = models.DateTimeField(default=datetime.now,blank=False)
    usuario = models.ForeignKey(
        to= User,
        on_delete= models.SET_NULL,
        null= True,
        blank= False,
        related_name= "user",
        )

    def __str__(self):
        return self.nome
