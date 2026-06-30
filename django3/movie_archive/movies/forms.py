from .models import Movies
from django.forms import ModelForm
from django import forms
class MoviesForm(ModelForm):
    class Meta:
        model = Movies
        fields = ['title','author','description','year','genre','poster']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':'Назва фільму'}),
            'author': forms.TextInput(attrs={'class':'form-control','placeholder':'Автор'}),
            'description': forms.Textarea(attrs={'class':'form-control','placeholder':'Опис'}),
            'year': forms.NumberInput(attrs={'class':'form-control','placeholder':'Рік'}),
            'genre': forms.TextInput(attrs={'class':'form-control','placeholder':'Жанр'}),
            'poster': forms.ClearableFileInput(attrs={'class':'form-control'})
        }