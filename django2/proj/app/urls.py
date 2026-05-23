from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('about',views.about),
    path('contacts',views.contacts),
    path('products',views.products),
    path('students',views.students),
    path('profile',views.profile)
]
