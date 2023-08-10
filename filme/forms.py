# página que eu criei para formulários

from django.contrib.auth.forms import UserCreationForm # formulário de criar usuário
from .models import Usuario
from django import forms


class FormHomepage(forms.Form): # personalizar o formulário padrão do django
    email = forms.EmailField(label=False)


class CriarContaForm(UserCreationForm):
    email = forms.EmailField() # adicionar o campo de email no banco de dados

    class Meta:   # obrigação do UserCreationForm para dizer o modelo de referência. Usuario é o nosso modelo próprio de gerenciar usuários
        model = Usuario
        fields = ('username', 'email', 'password1', 'password2')  # campos que serão exibidos no formulário quando criar uma conta