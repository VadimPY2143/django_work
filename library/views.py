from django.shortcuts import render, redirect
from .forms import AddBook
from .models import Book


def add_book(request):
    if request.method == 'POST':
        form = AddBook(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = AddBook
    return render(request, 'add_book.html', {'form': form})


def book_list(request):
    books = Book.objects.all()
    return render(request, 'main.html', {'books': books})


def search_books(request):
    query = request.GET.get('q')
    books = Book.objects.filter(title__icontains=query) | Book.objects.filter(author__icontains=query)
    return render(request, 'search_books.html', {'books': books, 'query': query})




