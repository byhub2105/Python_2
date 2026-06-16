from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('about',views.about),
    path('stats',views.stats),
    path('contacts',views.contacts)
]
