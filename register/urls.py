from django.urls import path, include
from requests import request

from .views import Register, Login
from django.http import HttpResponse
from register import views

urlpatterns = [
    path("login/", Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
    path("logout/", views.Logout, name="logout"),
    path('', include("django.contrib.auth.urls")),
    # path('',views.test, name='test'),
]
