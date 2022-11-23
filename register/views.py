from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.forms import UserCreationForm


def test (request):
    return HttpResponse("Test")


class Register(View):
    template_name = "register/register.html"
    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)
