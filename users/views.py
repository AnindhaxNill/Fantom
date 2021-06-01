from .forms import RegisterFrom
from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.views import  LoginView,LogoutView

# Create your views here.

class RegisterView(CreateView):
    template_name = 'users/register.html'
    form_class= RegisterFrom
    success_url = '/'


class UserLoginView(LoginView):
    template_name = 'users/login.html'

class UserLogoutView(LogoutView):
    template_name = 'users/login.html'



