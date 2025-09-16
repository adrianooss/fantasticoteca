from django.db import models
from datetime import datetime

# Represeta tabela no banco de dados
class Fotografia(models.Model):

    OPCOES_CATERORIA = [
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
    categoria = models.CharField(max_length=50, choices=OPCOES_CATERORIA ,default="")
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=100, null=False, blank=False)
    publicada = models.BooleanField(default=False)
    data_fotografia = models.DateTimeField(default=datetime.now,blank=False)


    def __str__(self):
        return f"Fotografia: {self.nome}"
