# weread/views.py

from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Book
from .serializers import BookSerializer


# List all books or create a new one
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# Retrieve, update, or delete a single book
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# Return the N most recently added books
class LastNBooksView(APIView):
    def get(self, request, n=5):
        latest_books = Book.objects.order_by("-added_at")[:n]
        serializer = BookSerializer(latest_books, many=True)
        return Response(serializer.data)
