from django.shortcuts import render
from .models import Categoria

# Create your views here.
def index(request):
    lista_categorias = Categoria.objects.all()
    context = {'lista_categorias':lista_categorias}
    return render(request, 'categorias/index', context)
