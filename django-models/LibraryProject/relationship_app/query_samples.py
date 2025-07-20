import os
import django

# Setup Django environment (run this if executing outside manage.py shell)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
def get_books_by_author(author_name):
    books = Book.objects.filter(author__name=author_name)
    return books

# 2. List all books in a library
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return []

# 3. Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.librarian  # Thanks to related_name
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None


# Sample usage (run only in interactive script or Django shell)
if __name__ == '__main__':
    print("Books by 'John Doe':", get_books_by_author('John Doe'))
    print("Books in 'Central Library':", get_books_in_library('Central Library'))
    print("Librarian of 'Central Library':", get_librarian_for_library('Central Library'))
# Ensure the 'relationships' app is included in the settings