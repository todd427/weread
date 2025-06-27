from django.shortcuts import render
from .models import shelfBook
from .serializers import shelfBookSerializer
from rest_framework import generics

def shelf_list(request):
    books = shelfBook.objects.all()
    return render(request, 'bookshelf/shelf_list.html', {'books': books})

def shelf_detail(request, pk):
    book = shelfBook.objects.get(pk=pk)
    return render(request, 'bookshelf/shelf_detail.html', {'book': book})

class BookListCreateView(generics.ListCreateAPIView):
    queryset = shelfBook.objects.all()
    serializer_class = shelfBookSerializer

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = shelfBook.objects.all()
    serializer_class = shelfBookSerializer