from rest_framework import serializers
from .models import Author, Book
import datetime


# THe relationship between Author and Book is one-to-many, so we can use a nested serializer for Books within the Author serializer.


# Basic serializers for Books
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']
    
    # Validation to ensure publication year is not in the future
    def validate(self, data):
        if data['publication_year'] > datetime.date.today():
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return data

# Serializer for Author with nested Bookss
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ['id', 'name', 'books']