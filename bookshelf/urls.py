# WeRead/urls.py
from django.urls import path
from .views import BookListCreateView, BookDetailView

urlpatterns = [
    path("bookshelf/list/", BookListCreateView.as_view(), name="book-list-create"),
    path("bookshelf/detail/<int:pk>/", BookDetailView.as_view(), name="book-detail"),
 
]