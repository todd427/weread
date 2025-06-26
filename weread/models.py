# WeRead/models.py
from django.db import models

class Book(models.Model):
    user = models.CharField(max_length=100, default="todd")
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=200, blank=True)
    isbn = models.CharField(max_length=20, blank=True)
    openlibrary_url = models.URLField(blank=True)
    googlebooks_url = models.URLField(blank=True)
    amazon_url = models.URLField(blank=True)
    date_acquired = models.DateField(null=True, blank=True)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.author}"
