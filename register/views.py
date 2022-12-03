from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm

from .forms import RegisterUserForm


class Register(CreateView):
    form_class = RegisterUserForm
    template_name = 'register/register.html'
    success_url = reverse_lazy('main')
