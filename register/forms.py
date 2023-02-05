from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import *


class RegisterUserForm(UserCreationForm, forms.ModelForm):
    class Meta(UserCreationForm.Meta):
        model = Custom_user
        fields = ('username', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': "register_input", 'placeholder': "test"},),
            'password1': forms.TextInput(attrs={'class': "register_input1", 'placeholder': "test"}),
            'password2': forms.TextInput(attrs={'class': "register_input2", 'placeholder': "test"}),
        }
