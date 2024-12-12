from django.contrib import admin
from django.urls import path, include
from .views import book_list, search_books, add_book

urlpatterns = [
    path('', book_list, name='book_list'),
    path('add_book/', add_book),
    path('search_books/', search_books, name='search_books'),
]