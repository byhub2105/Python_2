from django.shortcuts import render,redirect,get_object_or_404
from .models import Movies
from .forms import MoviesForm
from django.views.generic import DeleteView,UpdateView
def home(request):
    return render(request,'movies/home.html')
def movies(request):
    movies = Movies.objects.order_by('-id')
    return render(request,'movies/movies.html',{'movies':movies})
def add_movie(request):
    error=''
    if request.method == 'POST':
        movie = MoviesForm(request.POST, request.FILES)
        if movie.is_valid():
            movie.save()
            return redirect('movies')
        else:
            error = 'Форма не валідна'
    form = MoviesForm()
    data ={
        'form':form,
        'error':error
    }
    return render(request,'movies/movie_form.html',data)
def detail_movie(request,movie_id):
    movie = get_object_or_404(Movies, id=movie_id)
    context = {
        'movie':movie
    }
    return render(request,'movies/detail_movie.html',context)
class MovieDelete(DeleteView):
    model = Movies
    template_name = 'movies/delete_movie.html'
    success_url = '/movies/'
class MovieUpdate(UpdateView):
    model = Movies
    template_name = 'movies/movie_form.html'
    form_class = MoviesForm
    success_url ='/movies/'