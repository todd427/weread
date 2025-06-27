# WeRead/urls.py
from django.urls import path
from .views import BookListCreateView, BookDetailView, LastNBooksView

urlpatterns = [
    path("books/", BookListCreateView.as_view(), name="book-list-create"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="book-detail"),
    path("books/last/<int:n>/", LastNBooksView.as_view(), name="last-n-books"),
]
