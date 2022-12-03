from django.urls import path
from . import views
from .views import Main, Write, test
from . import views


urlpatterns = [
    path('', Main.as_view(), name='main'),
    path('write', Write.as_view(),name='write'),
    # path('test/',views.test,),
]

