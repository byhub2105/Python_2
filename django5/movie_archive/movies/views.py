from django.shortcuts import render,redirect,get_object_or_404
from .models import Movies,Profile,Comment
from .forms import MoviesForm,RegisterForm,LoginForm,ProfileForm,CommentForm
from django.contrib import messages
from django.views.generic import DeleteView,UpdateView
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
def get_or_create_profile(user):
    profile, _ =Profile.objects.get_or_create(user=user)
    return profile
def home(request):
    movies = Movies.objects.all()
    return render(request, 'movies/home.html', {'movies': movies})
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
def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            get_or_create_profile(user)
            login(request,user)
            messages.success(request,f'Вітаємо,{user.first_name}!')
            return redirect('home')
        messages.error(request,'Будь ласка переробіть форму')
    else:
        form = RegisterForm()
    return render(request,'movies/register.html',{'form':form})
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = LoginForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            get_or_create_profile(user)
            login(request,user)
            messages.success(request,f'З поверненням, {user.first_name or user.last_name}')
            return redirect(request.GET.get('next','home'))
        messages.error(request,'Невірний логін або пароль')
    else:
        form = LoginForm()
    return render(request,'movies/login.html',{'form':form})
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.info(request,'Ви успішно вийшли')
    return redirect('home')
@login_required
def comments_view(request, movie_id):
    movie = get_object_or_404(Movies, id=movie_id)
    comments = Comment.objects.filter(movie=movie) .order_by('-created_at')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.movie = movie
            comment.author = request.user
            comment.save()
            return redirect('comments', movie_id=movie.id)
    else:
        form = CommentForm()

    context = {
        'movie': movie,
        'comments': comments,
        'form': form
    }
    return render(request, 'movies/comments.html', context)
@login_required
def profile_view(request):
    profile = get_or_create_profile(request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES,instance=profile)
        form.fields['first_name'].initial = request.user.first_name
        form.fields['last_name'].initial = request.user.last_name
        form.fields['email'].initial = request.user.email
        if form.is_valid():
            request.user.first_name = form.cleaned_data['first_name']
            request.user.last_name = form.cleaned_data['last_name']
            request.user.email = form.cleaned_data['email']
            request.user.save()
            form.save()
            messages.success(request,'Профіль оновлено')
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile,initial={
            'first_name':request.user.first_name,
            'last_name':request.user.last_name,
            'email':request.user.email
        })
    return render(request,'movies/profile.html',{'form':form,'profile':profile})
@login_required
def delete_comment_view(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    movie_id = comment.movie.id  
    if comment.author == request.user:
        comment.delete()
    return redirect('comments', movie_id=movie_id)