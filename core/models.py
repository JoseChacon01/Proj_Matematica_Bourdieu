from django.db import models
from distutils.command.upload import upload
from django.contrib.auth.models import AbstractUser #Padrão

class Categorias_Usu(models.Model):
    tipo = models.CharField('Tipo', max_length=100) #Professor, pesquisador, aluno e administrador

class Usuarios(models.Model):
    nomeUsu =  models.CharField('NomeUsu', max_length=200)
    email = models.EmailField('Email')
    nascimento = models.DateField('Nascimento')
        
    class Meta:  
          permissions = [
            ("Administrador_1", "podera acessar a view da pagina usuarios"),
            ("Administrador_2", "podera acessar os Cruds principais"),
        ]

#Perfil não

class Acervo_Documentos(models.Model):
    data_acervos_docs = models.DateTimeField('Data_Acervo_Docs')
    autor = models.CharField('Autor', max_length=200)
    titulo = models.CharField('Titulo', max_length=200)
  # documento = models.BigAutoField('Documento')
  # categoria = models.Charfield('Categoria', max_lingth='100')

class Telefone_Usu (models.Model):
    telefone = models.CharField('Telefone', max_length=20)

class Endereco_Usu (models.Model):
    endereco = models.CharField('Endereco', max_length=200)
    numero = models.IntegerField('Numero')
    cep = models.IntegerField('CEP')

class Bairro_Usu (models.Model):
    bairro = models.CharField('Bairro', max_length=100)

class Cidade_Usu (models.Model):
    cidade = models.CharField('Cidade', max_length=100)

class Estado_Usu (models.Model):
    estado = models.CharField('Estado', max_length=100)

class Pais_Usu (models.Model):
    pais = models.CharField('pais', max_length=100)   




class Cadastros (models.Model):
    categoria_cadastro = models.CharField('Categoria_Cadastro', max_length=50)
    data_cadastro = models.DateTimeField('Data_Cadastro') 

class Noticias (models.Model):
    titulo_noticia = models.CharField('Titulo_Noticia', max_length=100)
    imagem_noticia = models.ImageField('Imagem_Noticia')
    descricao_noticia = models.CharField('Descricao_Noticia', max_length=600)

class Eventos (models.Model):
    Titu

class Pesquisador (models.Model):                











        