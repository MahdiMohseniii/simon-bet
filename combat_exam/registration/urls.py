from django.urls import path
from . import models, views
from django.conf import settings  
from django.conf.urls.static import static  
from payment.views import checkout, create_payment, payment_success, payment_cancel  


urlpatterns =[
    path('', views.FirstPage, name='home'),
    path('login/', views.Login_user, name='login'),
    path('logout/', views.Logout_user, name='logout'),
    path('signup/', views.signup_user, name='signup'),
    path('about/', views.about, name='about'),
    path('main/', views.main, name='main'),
    path('checkout/', checkout, name='checkout'),  
    path('payment/create/', create_payment, name='create_payment'),  
    path('payment/success/<int:amount>/', payment_success, name='payment_success'),  
    path('payment/cancel/', payment_cancel, name='payment_cancel'),  

]