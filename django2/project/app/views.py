from django.shortcuts import render,redirect

def main(request):
    return render(request,'app/main.html')
def home(request):
    return render(request,'app/index.html')
def about(request):
    return render(request,'app/about.html')