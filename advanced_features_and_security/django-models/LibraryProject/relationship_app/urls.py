from django.urls import path
from . import views
from .views import list_books, LibraryDetailView
from django.contrib.auth.views import LoginView, LogoutView
# from relationship_app.views import admin_view, librarian_view, member_view


urlpatterns =[
    # Public pages
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    
    # Implementing User Authentication
    path('login/', LoginView.as_view(template_name='relationship_app/login.html')),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html')),
    path('register/', views.register, name='register'),

    # Role-Based Pages
    # path('admin/', admin_view.admin_view, name='admin_view'),
    # path('librarian/', librarian_view.librarian_view, name='librarian_view'),
    # path('member/', member_view.member_view, name='member_view'),

    # Permission-Based Operations
    path('addbook/', views.add_book, name='add_book'),
    path('deletebook/', views.delete_book, name='delete_book'),
    path('editbook/', views.edit_book, name='edit_book'),
]