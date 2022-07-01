from django.urls import path
from .views import inicio, sobre_nosotros

urlpatterns = [
    path('', inicio, name= "inicio" ), 
    path('about/', sobre_nosotros , name= "sobre_nosotros" ), 
    
]