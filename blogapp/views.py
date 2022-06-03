from django.shortcuts import render

from blogapp.forms import AlumnosForm
from blogapp.models import Alumnos

# Create your views here.

def index(request):
    return render(request, "blogapp/index.html")

def readme(request):
    return render(request, "blogapp/readme.html")

def alta_alumno(request):
    if request.method == "POST":
        mi_form = AlumnosForm(request.POST)
        if mi_form.is_valid():
            datos = mi_form.cleaned_data
            alumno = Alumnos(nombre = datos["nombre"], pais = datos["pais"])
            alumno.save()
        return render(request, "blogapp/readme.html") 
    return render(request, "blogapp/readme.html")
        
    

"""
def about(request):
    return render(request, 'about.html')
"""