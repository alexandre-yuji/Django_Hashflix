from django.urls import path, reverse_lazy
from .views import Homepage, Homefilmes, DetalhesFilme, Pesquisafilme, Paginaperfil, Criarconta
from django.contrib.auth import views as auth_view  # dei novo nome para não confundir com as outras views que existem

app_name = 'filme' # nome do app para chamar nas urls do projeto hashflix, e não do projeto filme

urlpatterns = [
    # path('', homepage),  # caminho padrão do site, sem parâmetro na url. estou incluindo uma view chamada homepage. ou seja, chama a função homepage no arquivo views.py. estrutura Function Based View
    path('', Homepage.as_view(), name='homepage'), # chamo a classe Homepage como uma view do arquivo views.py. estrutura Class Based View
    path('filmes/', Homefilmes.as_view(), name='homefilmes'), # caminho para a tela de filmes, chamando a classe Homefilmes. name é para chamar a url nas tags <a href>
    path('filmes/<int:pk>', DetalhesFilme.as_view(), name='detalhesfilme'),  # chave primária do filme que eu quero, já que vem do object do model Detalhesfilme. caminho para a tela de detalhe do filme
    path('pesquisa/', Pesquisafilme.as_view(), name='pesquisafilme'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),  # LoginView é padrão do django, não precisei criar no views.py
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('editarperfil/<int:pk>', Paginaperfil.as_view(), name='editarperfil'),
    path('criarconta/', Criarconta.as_view(), name='criarconta'),
    path('mudarsenha/', auth_view.PasswordChangeView.as_view(template_name='editarperfil.html', success_url=reverse_lazy('filme:homefilmes')), name='mudarsenha'), # uso a editarperfil porque as funcionalidades das páginas são as mesmas
]