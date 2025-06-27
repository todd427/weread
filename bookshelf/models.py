from django.db import models

class shelfBook(models.Model):
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=300)
    asin = models.CharField(max_length=20, unique=True, null=True, blank=True)
    isbn = models.CharField(max_length=20, null=True, blank=True)
    source = models.CharField(max_length=100)  # e.g., "kindle", "epub", "openlibrary"
    date_added = models.DateTimeField(auto_now_add=True)
    cover_url = models.URLField(blank=True, null=True)
    metadata = models.JSONField(blank=True, null=True)
    amazon_url = models.URLField(blank=True, null=True)
    amazon_search_url = models.URLField(blank=True, null=True)
    date_acquired = models.DateField(null=True, blank=True)
    openlibrary_url = models.URLField(blank=True, null=True)
    googlebooks_url = models.URLField(blank=True, null=True)
    user = models.CharField(max_length=100, default='todd')
    date_read = models.DateField(null=True, blank=True)
    rating = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        help_text="Optional rating from 1 to 5"
    )


    # 🆕 Read tracking and evaluation
    date_read = models.DateField(null=True, blank=True)
    rating = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        help_text="Optional rating from 1 to 5"
    )
    
    def __str__(self):
        return f"{self.title} by {self.author}"

