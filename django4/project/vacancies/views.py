from django.shortcuts import render,redirect

from .models import Vacancies
from .forms import VacanciesForm
from .services import parse_jooble
from django.views.generic import DeleteView,UpdateView
from django.core.paginator import Paginator
from django.contrib import messages
def vacancies(request):
    qs = Vacancies.objects.order_by('-id')
    search = request.GET.get('q')
    if search:
        qs = qs.filter(title__icontains=search)
    paginator = Paginator(qs,10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'vacancies/index.html', {'page_obj':page_obj})
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
def parse_jooble_view(request):
    added = parse_jooble()
    messages.success(request,f'Імпортовано {added} вакансій')
    return redirect('vacancies')