from django.shortcuts import render
from django.views.generic import CreateView
def home(request):
    return render(request, 'home.html')

def contact_us(request):
    return render(request, 'contact_us.html')

def about_us(request):
    return render(request, 'about_us.html')

