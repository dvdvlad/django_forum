from django.contrib.sites import requests
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView
from django.views.generic import ListView
from django.shortcuts import render
from .forms import Articles_forms
from .models import Articles


def test (request):
    return render (request ,'main/register/register.html')


class Main(ListView):
    template_name = 'main/index.html'
    model = Articles
    context_object_name = "news"


class Write(CreateView):
    template_name = 'main/write.html'
    form_class = Articles_forms
    success_url = '/'

