<!-- Cretae -->
new_book = Book(title='1984', author='George Orwell', publication_year=1949)
new_book.save()
<!-- Output:  -->

<!-- Retrieve -->
Book.objects.all()
<!-- Output: <QuerySet [<Book: Book object (1)>]> -->

<!-- Update -->
book = Book.objects.get(id=1)
book.title = 'Nineteen Eighty-Four'
book.save()
<!-- Output:  -->

<!-- Delete -->
book.delete()
<!-- Output: (1, {'bookshelf.Book': 1}) -->
