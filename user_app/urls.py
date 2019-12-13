from django.contrib import admin
from django.urls import path, include
from .views import login, logout


urlpatterns = [
    path('login/', login, name='user.login'),
    path('logout/', logout, name='user.logout')
]
