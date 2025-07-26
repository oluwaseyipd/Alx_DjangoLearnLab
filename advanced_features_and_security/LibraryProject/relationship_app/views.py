from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from .forms import BookForm, UserRegisterForm, UserLoginForm
from django.contrib.auth.decorators import permission_required


# 1. Listing all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# 2. Displays details for a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
 
# 3. Register
def register(request):
    if request.method == 'POST':
         form = UserRegisterForm(request.POST)
         if form.is_valid():
              user = form.save()
              return redirect('login')
    else:
         form = UserRegisterForm()
    return render(request, 'relationship_app/register.html')

# 4. Login View
def login_view(request):
    return render(request, 'relationship_app/login.html')

# 5. Logout View
def logout_view(request):
        return render(request, 'relationship_app/logout.html')


# 6. Edit Books
@permission_required('relationship_app.can_edit_book')
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('relationship_app/list_book.html')
    else:
        form = BookForm(instance=book)
    return render(request, 'relatioship_app/edit_book.html')
           


# 7. Add Books
@permission_required('relationship_app.can_add_book')
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('relationship_app/list_book.html')
    else:
                form = BookForm()
    return render(request, 'relatioship_app/add_book.html')

# 8. Delete Books
@permission_required('relationship_app.can_delete_book')
def delete_book(request):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('relationship_app/list_book.html')
    return render(request, 'relatioship_app/list_book.html')


# 9. Role checkers
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

