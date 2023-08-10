from django.contrib import admin
from .models import Filme, Episodio, Usuario  # . é porque eu importo models.py que está na mesma pasta do admin.py. Filme é a classe filme do models.py. Na página de admin aparece como Filmes.
from django.contrib.auth.admin import UserAdmin # gerencia os usuários

# Register your models here.
# Registrar os modelos para aparecerem na página de admin

# essa parte só existe porque eu quero que apareça no admin o campo personalizado filmes_vistos
campos = list(UserAdmin.fieldsets) # editar os campos que o UserAdmin vai exibir além dos padrões do django transformado em lista
campos.append(
    ("Histórico", {'fields': ('filmes_vistos',)})  # # Histórico é o nome da seção que eu to criando no admin, filmes_vistos é o nome do campo que eu dei na classe Usuario do models.py
)
UserAdmin.fieldsets = tuple(campos) # devolvo a lista para o admin


admin.site.register(Filme)
admin.site.register(Episodio)
admin.site.register(Usuario, UserAdmin) # gerencia login, as sessões, janelas abertas