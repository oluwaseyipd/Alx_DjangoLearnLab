from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book

def home(request):
    return render(request, 'bookshelf/home.html')

@permission_required('your_app_name.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('your_app_name.can_create', raise_exception=True)
def create_book(request):
    # Example placeholder code for creating a book
    if request.method == "POST":
        # process form
        pass
    return render(request, 'bookshelf/create_book.html')

@permission_required('your_app_name.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    # implement edit logic
    return render(request, 'bookshelf/edit_book.html', {'book': book})

@permission_required('your_app_name.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    # implement delete logic
    return render(request, 'bookshelf/delete_book.html', {'book': book})
