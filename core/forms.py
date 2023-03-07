from dataclasses import fields
from .models import Usuario
from .models import Categoria
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm



class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome'] 

class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'password1', 'password2', 'email', 'nome', 'idade', 'cpf', 'categoria']        