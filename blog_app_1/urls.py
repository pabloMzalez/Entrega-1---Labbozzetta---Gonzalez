from django.urls import path
from .views import inicio, sobre_nosotros, crear_blog

urlpatterns = [
    path('', inicio, name= "inicio" ), 
    path('about/', sobre_nosotros , name= "sobre_nosotros" ), 
    path('blog/', crear_blog , name= "crear_blog" ), 
]