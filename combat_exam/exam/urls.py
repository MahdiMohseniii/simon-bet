# exam/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.exam_start, name='exam_start'),
    path('question/', views.exam_question, name='exam_question'),
    path('results/', views.exam_results, name='exam_results'),
]
