from unicodedata import name
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# vista acerca de nosotros, home y listas   (donde iria el formulario de busqueda y creacion de modelos)

def inicio(request):
    return render(request,"inicio.html")

def sobre_nosotros(request):
    return render(request, "sobre_nosotros.html")



def crear_blog(request):
    #acceso al formulario creado con django 
    
  
    
    return render(request, "blog.html")
    

    
def listado_blog(request):
    ...