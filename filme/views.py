from django.shortcuts import render, redirect, reverse  # renderiza uma página, redireciona para uma página, pega o link de uma página
from .models import Filme, Usuario
from .forms import CriarContaForm, FormHomepage
from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView # exibe templates, exibe listas, exibe detalhes de um item, exibe um formulário, reconhece a tabela que estou usando e carrega os campos que eu definir
from django.contrib.auth.mixins import LoginRequiredMixin # classe que bloqueia as classes da estrutura Class Based View que não estão logadas
                                                          # a autenticação do login está no settings.py

# Create your views here.

class Homepage(FormView): # herda a biblioteca FormView  # estrutura Class Based View # objetivo é mostrar uma view
    template_name = "homepage.html"  # nome do template que eu estou chamando com a classe
    form_class = FormHomepage

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated: # se o usuário está autenticado, redireciona para a homefilmes se tentar entrar na homepage. se não estiver logado, entra na homepage para fazer login
            return redirect('filme:homefilmes')  # não é carregar/render um template, é redirecionar para outra view. nome do app e nome da url definido em filme/urls.py
        else:
            return super().get(request, *args, **kwargs) # redireciona o usuário para a homepage

    def get_success_url(self):
        email = self.request.POST.get("email") # pega a informação passada do campo email vindo do post
        usuarios = Usuario.objects.filter(email=email) # verifica a lista de emails no banco de dados

        if usuarios:
            return reverse('filme: login') # se existir, manda pra página de login
        else:
            return reverse('filme:criarconta') # se não existir, manda pra página de criar conta


class Homefilmes(LoginRequiredMixin, ListView): # objetivo é exibir uma lista de itens
    template_name = "homefilmes.html"
    model = Filme  # model do banco de dados que eu quero pegar a lista. o nome da lista é padrão object_list. os objetos são de acordo com o model que eu importei: Filme são filmes, Episódios são episódios...


class DetalhesFilme(LoginRequiredMixin, DetailView): # exibir detalhes do filme, como imagem, nome, descrição, data de criação
    template_name = "detalhesfilme.html"
    model = Filme  # o nome do objeto é padrão object. um objeto.

    def get_context_data(self, **kwargs): # função padrão da estrutura Class Based View para adicionar um lista relacionada em UMA determinada view, nesse caso a DetailView
        context = super(DetalhesFilme, self).get_context_data(**kwargs) # linha de código obrigatória

        filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)[0:5]  # filtrar a tabela de filmes pegando os filmes que a categoria é a mesma do filme da página(object) pegando até 5. ex: programação, análises, apresentação.
        context["filmes_relacionados"] = filmes_relacionados # variável filmes_relacionados com a chave do dicionário filmes_relacionados que vai para o html

        return context

    def get(self, request, *args, **kwargs):  # função para pegar quando alguém entrou na página do filme e contabilizar uma visualização
        filme = self.get_object() # filme que o usuário está acessando
        filme.visualizacoes += 1
        filme.save() # salvo no banco de dados que o filme foi acessado e adicionado uma vizualização

        usuario = request.user  # pego o usuário que está logado
        usuario.filmes_vistos.add(filme)  # adiciono um campo do banco de dados com o filme que o usuário entrou na página e contabilizou como uma visuzalização

        return super(DetalhesFilme, self).get(request, *args, **kwargs) # redireciona o usuário para a url final

class Pesquisafilme(LoginRequiredMixin, ListView): # o resultado é uma lista de itens
    template_name = "pesquisa.html"
    model = Filme

    def get_queryset(self):  # função para buscar/filtrar uma informação no campo de pesquisa
        termo_pesquisa = self.request.GET.get('query') # pego o que tiver no parâmetro query lá do formulário do campo de pesquisa no navbar.html

        if termo_pesquisa:
            object_list = self.model.objects.filter(titulo__icontains=termo_pesquisa)   # nome padrão do que vem de uma ListView. self.model já referencia o model Filme da classe. titulo__icontains procura na lista o que tem parecido com aquele termo, no caso o que está na variável termo_pesquisa que vem do campo de pesquisa
            return object_list
        else:
            return None


class Paginaperfil(LoginRequiredMixin, UpdateView):
    template_name = "editarperfil.html"
    model = Usuario
    fields = ['first_name', 'last_name', 'email']

    def get_success_url(self):
        return reverse('filme:homefilmes')


class Criarconta(FormView):
    template_name = "criarconta.html"
    form_class = CriarContaForm

    def form_valid(self, form):
        form.save() # verifica se as informações foram preenchidas corretamente e salva no banco de dados
        return super().form_valid(form)

    def get_success_url(self):  # se o formulário de criação estiver certo, o que vai ser feito
        return reverse('filme:login') # a função pede como resposta o texto de um link (reverse)





# def homepage(request):    # estrura Function Based View
#     return render(request, "homepage.html")  # retorna um template/página html. request é padrão do render

# def homefilmes(request):
#     context = {}
#     lista_filmes = Filme.objects.all() # pego todos os itens do models Filme
#     context['lista_filmes'] = lista_filmes # cria uma chave de dicionário
#     return render(request, "homefilmes.html", context) # context é uma forma usando view com uma lista/dicionário