from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.exceptions import ValidationError
# Create your views here.


# BookListView: Returns a list of all Book instances.
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# BookDetailView: Returns details for a single Book instance.
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# BookCreateView: Allows authenticated users to create a new Book.
# - Custom validation: Prevents duplicate titles.
# - Permissions: Only authenticated users can create; others can read.
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        
        title = serializer.validated_data.get('title')
        if Book.objects.filter(title=title).exists():
            raise ValidationError({"title": "Book with this title already exists."})
        serializer.save()    

# BookUpdateView: Allows authenticated users to update an existing Book.
# - Custom validation: Prevents duplicate titles (excluding current instance).
# - Permissions: Only authenticated users can update.
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
         # Custom hook: Check for duplicate title, excluding current book.
        title = serializer.validated_data.get('title')
        if Book.objects.filter(title=title).exclude(pk=serializer.instance.pk).exists():
            raise ValidationError({"title": "Book with this title already exists."})
        serializer.save()

# BookDeleteView: Allows authenticated users to delete a Book instance.
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer