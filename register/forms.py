from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Custom_user


class RegisterUserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Custom_user
        fields = ('username', 'password1', 'password2')