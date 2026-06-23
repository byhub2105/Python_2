from django.shortcuts import render,redirect

from .models import Vacancies
from .forms import VacanciesForm
def vacancies(request):
    vacancies = Vacancies.objects.order_by('-id')
    return render(request,'vacancies/index.html', {'vacancies':vacancies})
def add_vacancy(request):
    error=''
    if request.method == 'POST':
        form = VacanciesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vacancies')
        else:
            error = 'Форма не валідна'
    form = VacanciesForm()
    data ={
        'form':form,
        'error':error
    }
    return render(request,'vacancies/add_vacancy.html',data)