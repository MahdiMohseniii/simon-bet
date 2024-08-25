from django.urls import path
from . import models, views

urlpatterns =[
    path('', views.FirstPage, name='home'),
]