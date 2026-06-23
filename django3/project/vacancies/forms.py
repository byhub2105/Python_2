from .models import Vacancies
from django.forms import ModelForm
from django import forms
class VacanciesForm(ModelForm):
    class Meta:
        model = Vacancies
        fields =['title','description','salary','company','location']
        widgets ={
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':'Назва вакансії'}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':'Опис'}),
            'salary': forms.NumberInput(attrs={'class':'form-control','placeholder':'Зарплата'}),
            'company': forms.TextInput(attrs={'class':'form-control','placeholder':'Компанія'}),
            'location': forms.TextInput(attrs={'class':'form-control','placeholder':'Місто'})               
        }