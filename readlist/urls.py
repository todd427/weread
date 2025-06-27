# readinglist/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("weread.urls")),
    path("api/", include("bookshelf.urls")),
]
