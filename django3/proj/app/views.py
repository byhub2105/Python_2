from django.shortcuts import render

def home(request):
    return render(request,'app/index.html')
def about(request):
    return render(request,'app/about.html')
def stats(request):
    return render(request,'app/stats.html')
def contacts(request):
    return render(request,'app/contacts.html')