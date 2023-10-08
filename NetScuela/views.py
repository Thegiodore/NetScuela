from django.shortcuts import render
from django.views.generic import CreateView
def index(request):
    return render(request, 'home.html')

