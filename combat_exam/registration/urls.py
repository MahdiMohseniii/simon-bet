from django.urls import path
from . import models, views
from django.conf import settings  
from django.conf.urls.static import static  

urlpatterns =[
    path('', views.FirstPage, name='home'),
    path('login/', views.Login_user, name='login'),
    path('logout/', views.Logout_user, name='logout'),
    path('signup/', views.signup_user, name='signup'),
    path('about/', views.about, name='about'),
]