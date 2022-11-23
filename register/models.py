from django.db import models
from django.contrib.auth.models import User
from django.db import models


class Custom_user(User):
        favorites = models.SlugField('Избраное')