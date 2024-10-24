from django.shortcuts import render
from .models import Articulo

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')


def articulos_list(request):
    #obtiene todos los articulos de BBDD
    articulos = Articulo.objects.all()
    return render(request, 'blog/articulos_list.html', {'articulos': articulos})
 

