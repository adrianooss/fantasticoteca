from django.db import models

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


    def __str__(self):
        return f"Fotografia: {self.nome}"
    