from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import ListView
from django.shortcuts import render
from .forms import Articles_forms
from .models import Articles


def test (request):
    return render (request ,'main/register/register.html')


class main(ListView):
    template_name = 'main/index.html'
    model = Articles
    context_object_name = "news"


class write(CreateView):
    form_class = Articles_forms
    template_name = 'main/write.html'
    success_url = reverse_lazy('main')