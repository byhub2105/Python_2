from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.vacancies, name='vacancies'),
    path('add/',views.add_vacancy,name='add_vacancy')
]