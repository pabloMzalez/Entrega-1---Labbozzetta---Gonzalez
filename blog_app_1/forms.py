from django import forms

class FormBlog(forms.Form):
    titulo = forms.CharField(max_length= 50)
    contenido = forms.CharField(max_length= 500)
    fecha_creacion = forms.DateField(required=False)
    
