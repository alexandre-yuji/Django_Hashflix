from django.db import models
from django.utils import timezone  # permite utilizar a data atual de uma ação
from django.contrib.auth.models import AbstractUser # importo o usuário padrão do django para poder modificá-lo do meu jeito de criar usuário

# Create your models here. Meu banco de dados!

LISTA_CATEGORIAS = (   # necessária para o campo categoria. (1º o que armazena no banco, 2º o que aparece pro usuário)
    ("ANALISES", "Análises"),
    ("PROGRAMACAO", "Programação"),
    ("APRESENTACAO", "Apresentação"),
    ("OUTROS", "Outros"),
)

# criar o filme
class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='thumb_filmes')  # nome da pasta que armazena as imagens que o usuário criar dos filmes
    descricao = models.TextField(max_length=1000)
    categoria = models.CharField(max_length=15, choices=LISTA_CATEGORIAS)
    visualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo  # retorno na página de admin o atributo título, ao invés de aparecer Filme.object como nome


# criar episódios
class Episodio(models.Model):
    filme = models.ForeignKey("Filme", related_name="episodios", on_delete=models.CASCADE) # relação do episódio com o filme, o episódio só pode pertencer a um filme. o parâmetro é o nome da tabela que está criando a relação. related_name "cria" um campo na tabela Filme com todos os episódios que aquele filme tem. se eu deletar o Filme, deleto todos os episódios dele
    titulo = models.CharField(max_length=100)
    video = models.URLField() # se comporta como um link

    def __str__(self):
        return self.filme.titulo + " - " + self.titulo  # retorno na página de admin o atributo título, ao invés de aparecer Episodio.object como nome


class Usuario(AbstractUser):
    filmes_vistos = models.ManyToManyField("Filme") # vários usuários podem ver um filme e um filme pode ser visto por vários usuários, passando a classe Filme