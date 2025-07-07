from django.contrib import admin
from .models import Book

# Custom admin configuration
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns to show in list view
    list_filter = ('author', 'publication_year')  # Sidebar filters
    search_fields = ('title', 'author')  # Search bar fields

# Register the model with the custom admin
admin.site.register(Book, BookAdmin)
