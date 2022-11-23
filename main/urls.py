from django.urls import path
from . import views
from .views import main, write, test
from . import views


urlpatterns = [
    path('', main.as_view(), name='main'),
    path('write', write.as_view(), name='write'),
    path('test/',views.test,),
]

