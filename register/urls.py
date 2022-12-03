from django.urls import path, include
from .views import  Register
from django.http import HttpResponse
from register import views


urlpatterns = [
    path('register', Register.as_view(), name='register'),
    path('',include("django.contrib.auth.urls")),
    # path('',views.test, name='test'),
]