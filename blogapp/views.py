from django.shortcuts import render
from django.http import HttpResponse
from blogapp.forms import AlumnosForm
from blogapp.forms import GraduadosForm
from blogapp.forms import CursosForm
from blogapp.models import Alumnos, Cursos, Graduados

# Create your views here.

def index(request):
    return render(request, "blogapp/index.html")

def home(request):
    return render(request, "blogapp/home.html")

def readme(request):
    return render(request, "blogapp/readme.html")

def alta_alumno(request):
    if request.method == "POST":
        mi_form = AlumnosForm(request.POST)
        if mi_form.is_valid():
            datos = mi_form.cleaned_data
            alumno = Alumnos(nombre = datos["nombre"], pais = datos["pais"])
            alumno.save()
        return render(request, "blogapp/alumnos.html") 
    return render(request, "blogapp/alumnos.html")

def alta_cursos(request):
    if request.method == "POST":
        mi_form = CursosForm(request.POST)
        if mi_form.is_valid():
            datos = mi_form.cleaned_data
            curso = Cursos(nombre = datos["nombre"], area = datos["area"])
            curso.save()
        return render(request, "blogapp/cursos.html") 
    return render(request, "blogapp/cursos.html")

def alta_graduados(request):
    if request.method == "POST":
        mi_form = GraduadosForm(request.POST)
        if mi_form.is_valid():
            datos = mi_form.cleaned_data
            graduados = Graduados(nombre = datos["nombre"], nota = datos["nota"])
            graduados.save()
        return render(request, "blogapp/graduados.html") 
    return render(request, "blogapp/graduados.html")
        

def buscar_alumnos(request):
    return render( request , "blogapp/buscar_alumnos.html" )

    
"""
def buscar(request):
    if  request.method == 'GET'
        #request.POST.get("nombre", False) == "nombre": #request.GET['nombre']:#request.POST.get("nombre", False) == "nombre": 
        nombre = request.GET['nombre']
        alumnos = Alumnos.objects.filter(nombre__icontains = nombre)
        return HttpResponse({"alumnos": alumnos})#render(request, "blogapp/resultado_busqueda.html", {"alumnos": alumnos})
    else:
        return HttpResponse("No encontre") #render(request, "blogapp/buscar_alumnos.html")
"""

def buscar(request):
    if request.method == 'GET':
        nombre = request.GET.get('nombre')
    if nombre:
        alumnos = Alumnos.objects.filter(nombre__icontains=nombre)
        return render(request, 'blogapp/resultado_busqueda.html', {'alumnos': alumnos})
    else:
        print('Nada para mostrar')
        return request(request, 'blogapp/home.html', {})
    
