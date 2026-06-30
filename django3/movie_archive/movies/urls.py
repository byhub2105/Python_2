from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('',views.home, name='home'),
    path('movies/',views.movies, name='movies'),
    path('add_movie/',views.add_movie, name='add_movie'),
    path('detail/<int:movie_id>/',views.detail_movie, name='detail'),
    path('<int:pk>/update',views.MovieUpdate.as_view(),name='update'),
    path('<int:pk>/delete',views.MovieDelete.as_view(),name='delete')
]
