from django.contrib import admin
from django.urls import path, include

from qna_app import views

urlpatterns = [
    path('', views.index, name='qna.index'),
    path('add/', views.add_question, name='qna.add'),
    path('detail/<int:id>', views.detail, name='qna.detail'),
    path('faker/', views.faker, name='faker')
]
