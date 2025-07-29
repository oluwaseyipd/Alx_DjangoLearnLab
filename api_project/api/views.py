from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from .serializers import BookSerializer
from .models import Book

# Create your views here.
class BookList(generics.ListAPIView):
    # queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = queryset = Book.objects.all()
        name_filter = self.request.query_params.get('name', None)
        if name_filter is not None:
            queryset = queryset.filter(name__icontains=name_filter)
        return queryset

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        name_filter = self.request.query_params.get('name', None)
        if name_filter is not None:
            queryset = queryset.filter(name__icontains=name_filter)
        return queryset
