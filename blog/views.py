from django.shortcuts import render

# Create your views here

# Inclui a classe HttpResponse.
from django.http import HttpResponse

#Define uma function viem chamada index.
def index(request):
    #return HttpResponse('Olá Django - index')
    return render(request, 'index.html', {'titulo': 'Últimos Artigos'})
 
# Define uma function view chamada ola.
def ola(request):
    return HttpResponse('Olá Django')