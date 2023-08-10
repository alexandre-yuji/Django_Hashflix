# arquivo criado por mim, não é padrão do django
# gerenciador de contextos, serve para armazenar as variáveis que eu tenho acesso dentro do código html

from .models import Filme

def lista_filmes_recentes(request):
    lista_filmes = Filme.objects.all().order_by('-data_criacao')[0:8]  # lista definida que percorre o banco de dados (Filme). estou pegando todos os filmes de Filmes e ordenando pela data_criacao (campo no banco de dados) em negativo para ser decrescente, já que o python considera as datas como números que vão aparecendo em relação a uma data inicial padrão

    if lista_filmes:
        filme_destaque = lista_filmes[0]
    else:
        filme_destaque = None

    return {"lista_filmes_recentes": lista_filmes, "filme_destaque": filme_destaque}  # obrigatório retorna um dicionário. chave é o nome da variável que vai pro html e retorna a lista que eu criei

def lista_filmes_em_alta(request):
    lista_filmes = Filme.objects.all().order_by('-visualizacoes')[0:8]  # lista definida que percorre o banco de dados (Filme). estou pegando todos os filmes de Filmes e ordenando pelas visualizações (campo no banco de dados) em negativo para ser decrescente, já que o python considera as datas como números que vão aparecendo em relação a uma data inicial padrão
    return {"lista_filmes_em_alta": lista_filmes}



# def filme_destaque(request):
#     lista_filmes = Filme.objects.order_by('-data_criacao')[0]
#     return {"filme_destaque": filme}



# para conectar os context no projeto, foi adicionado no arquivo settings.py, na parte de TEMPLATE