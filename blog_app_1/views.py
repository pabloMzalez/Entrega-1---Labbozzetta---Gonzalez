from datetime import datetime
from unicodedata import name
from django.template import loader
from django.shortcuts import redirect, render
from django.http import HttpResponse

from blog_app_1.forms import BusquedaBlog, FormBlog
from blog_app_1.models import Blog

# Create your views here.

# vista acerca de nosotros, home y listas   (donde iria el formulario de busqueda y creacion de modelos)

def inicio(request):
    return render(request,"inicio.html")

def sobre_nosotros(request):
    return render(request, "sobre_nosotros.html")



def crear_blog(request):
    #acceso al formulario creado con django 
    if request.method == "POST":
        form = FormBlog(request.POST)
                        
        if form.is_valid():
            data = form.cleaned_data
                
            fecha = data.get("fecha_creacion") 
            if not fecha:
                fecha = datetime.now()
            
            entrada = Blog(titulo = data.get("titulo"), 
                            contenido = data.get("contenido"),
                            fecha_creacion = fecha)
            entrada.save()
           
            
            return redirect("listado_blog")
        else:
            return render(request, "blog.html", {"form": form}) 
        
    entrada = FormBlog()
    return render(request, "blog.html", {"form": entrada})
    

    
def listado_blog(request):
    titulo_de_busqueda = request.GET.get("titulo")
    
    if titulo_de_busqueda:
        listado_blog = Blog.objects.filter(titulo__icontains = titulo_de_busqueda)
    else:
        listado_blog = Blog.objects.all()
    
     
    form = BusquedaBlog()
    return render(request, "busqueda_blog.html", {"listado_blog": listado_blog,"form":form})
