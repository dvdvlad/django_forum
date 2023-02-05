import django.contrib.auth.forms
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegisterUserForm
from django.contrib.auth.forms import AuthenticationForm

class Register(CreateView):
    form_class = RegisterUserForm
    template_name = 'register/register.html'
    success_url = reverse_lazy('main')


class Login(LoginView):
    template_name = "register/login.html"
    form_class = AuthenticationForm


def Logout(request):
    logout(request)
    return redirect('main')
    pass
