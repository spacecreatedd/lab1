from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from . import forms
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import logout


def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

@login_required()
def profile(request):
    return render(request, 'web/profile.html')

def login(request):
    return render(request, 'registration/login.html')

def register(request):
    return render(request, 'registration/register.html')



#Авторизация, вход и выход
class RegisterUserView(CreateView):
    model = User
    form_class = forms.RegisterUserForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")

class LoginUserView(LoginView):
    template_name = "registration/login.html"

def logout_view(request):
    logout(request)
    return redirect("login")
