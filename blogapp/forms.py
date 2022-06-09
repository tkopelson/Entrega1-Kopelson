from django import forms

class AlumnosForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    pais = forms.CharField(max_length=40)

class GraduadosForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    nota = forms.IntegerField()

class CursosForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    area = forms.CharField(max_length=30)

