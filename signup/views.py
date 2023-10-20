from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import SignUp
from .forms import SignUpModelForm, LogInModelForm


class SignUpCreateView(CreateView):
    form_class = SignUpModelForm
    template_name = "create_view.html"
    if(SignUp.password1 == SignUp.password2):
        success_url = "todo/"
    else:
        success_url = "account/signup"


class LoginCreateView(CreateView):
    form_class = LogInModelForm
    template_name = "login.html"
    success_url = "/"
# Create your views here.
