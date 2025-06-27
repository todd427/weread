# bookshelf/serializers.py
from rest_framework import serializers
from .models import shelfBook

class shelfBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = shelfBook
        fields = "__all__"
