from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home),
    path('about/<int:vacancy_id>/',views.about, name='about')
]
