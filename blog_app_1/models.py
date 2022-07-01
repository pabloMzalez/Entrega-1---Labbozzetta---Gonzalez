
from django.db import models

# Create your models here.
class Blog(models.Model):
    titulo = models.CharField(max_length= 50)
    contenido = models.CharField(max_length= 500)
    fecha_creacion = models.DateField(null=True)
    
    def __str__(self):
        return f"{self.titulo}"