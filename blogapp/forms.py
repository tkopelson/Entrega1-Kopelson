from django import forms

class AlumnosForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    pais = forms.CharField(max_length=40)

