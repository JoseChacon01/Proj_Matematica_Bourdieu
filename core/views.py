from django.shortcuts import render

def home (resquest):
    return render(resquest, "index.html")

def cadastro(resquest):
    return render(resquest, "cadstro.html")

def noticias(resquest):
    return render(resquest, "noticias.html") 
# Create your views here.
