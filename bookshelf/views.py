from django.shortcuts import render
from .models import shelfBook

def book_list(request):
    books = shelfBook.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

def book_detail(request, pk):
    book = shelfBook.objects.get(pk=pk)
    return render(request, 'bookshelf/book_detail.html', {'book': book})
