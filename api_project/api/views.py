from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .serializers import BookSerializer
from .models import Book

# Create your views here.
class BookList(ListCreateAPIView):
    # queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = queryset = Book.objects.all()
        name_filter = self.request.query_params.get('name', None)
        if name_filter is not None:
            queryset = queryset.filter(name__icontains=name_filter)
        return queryset
