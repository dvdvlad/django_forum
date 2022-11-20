from .models import Articles
from django.forms import ModelForm


class Articles_forms(ModelForm):
    class Meta:
        model = Articles
        fields = ['articles', 'text']
