from django.contrib import admin
from django.urls import path, include
from Auth.views import user_logout, user_login, register

urlpatterns = [
    path('register/', register),
    path('login/', user_login),
    path('logout/', user_logout)
]