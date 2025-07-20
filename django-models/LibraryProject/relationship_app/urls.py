# relationship_app/urls.py
from django.urls import path
from .views import list_books, LibraryDetailView
from .views import register_view, login_view, logout_view
from .views import register_view, CustomLoginView, CustomLogoutView

urlpatterns = [
    path('books/', list_books, name='list_books'),  # function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # class-based view
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', register_view, name='register'),
]
