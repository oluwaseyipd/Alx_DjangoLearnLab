# Advanced API Project - Views Documentation

This project provides a RESTful API for managing `Book` instances using Django REST Framework (DRF). Below is a summary of each view, its configuration, and custom logic.

---

## Views Overview

### 1. BookListView
- **Type:** `ListAPIView`
- **Purpose:** Returns a list of all Book instances.
- **Permissions:** Open to all users (read-only).
- **Configuration:**  
  ```python
  class BookListView(generics.ListAPIView):
      queryset = Book.objects.all()
      serializer_class = BookSerializer
  ```

### 2. BookDetailView
- **Type:** `RetrieveAPIView`
- **Purpose:** Returns details for a single Book instance.
- **Permissions:** Open to all users (read-only).
- **Configuration:**  
  ```python
  class BookDetailView(generics.RetrieveAPIView):
      queryset = Book.objects.all()
      serializer_class = BookSerializer
  ```

### 3. BookCreateView
- **Type:** `CreateAPIView`
- **Purpose:** Allows authenticated users to create a new Book.
- **Permissions:** Only authenticated users can create; others can read.
- **Custom Hook:**  
  - **Duplicate Title Validation:** Prevents creation of books with duplicate titles.
  - **Method:** `perform_create`
  - **Logic:**  
    ```python
    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        if Book.objects.filter(title=title).exists():
            raise ValidationError({"title": "Book with this title already exists."})
        serializer.save()
    ```
- **Configuration:**  
  ```python
  class BookCreateView(generics.CreateAPIView):
      queryset = Book.objects.all()
      serializer_class = BookSerializer
      permission_classes = [IsAuthenticatedOrReadOnly]
  ```

### 4. BookUpdateView
- **Type:** `UpdateAPIView`
- **Purpose:** Allows authenticated users to update an existing Book.
- **Permissions:** Only authenticated users can update.
- **Custom Hook:**  
  - **Duplicate Title Validation:** Prevents updating a book to a title that already exists (excluding the current instance).
  - **Method:** `perform_update`
  - **Logic:**  
    ```python
    def perform_update(self, serializer):
        title = serializer.validated_data.get('title')
        if Book.objects.filter(title=title).exclude(pk=serializer.instance.pk).exists():
            raise ValidationError({"title": "Book with this title already exists."})
        serializer.save()
    ```
- **Configuration:**  
  ```python
  class BookUpdateView(generics.UpdateAPIView):
      queryset = Book.objects.all()
      serializer_class = BookSerializer
      permission_classes = [IsAuthenticatedOrReadOnly]
  ```

### 5. BookDeleteView
- **Type:** `DestroyAPIView`
- **Purpose:** Allows authenticated users to delete a Book instance.
- **Permissions:** Only authenticated users can delete.
- **Configuration:**  
  ```python
  class BookDeleteView(generics.DestroyAPIView):
      queryset = Book.objects.all()
      serializer_class = BookSerializer
  ```

---

## Custom Settings & Hooks

- **Permissions:**  
  All create, update, and delete operations require authentication (`IsAuthenticatedOrReadOnly`).
- **Validation:**  
  Custom validation in `perform_create` and `perform_update` prevents duplicate book titles.
- **Error Handling:**  
  If a duplicate title is detected, a `ValidationError` is raised with a clear message.

---

## Usage

- **List & Retrieve:** Accessible to all users.
- **Create, Update, Delete:** Require authentication (provide a valid token).
- **Validation:** Duplicate titles are not allowed for creation or update.

---

## Testing

Use tools like Postman or `curl` to


## Filtering, Searching, and Ordering in BookListView

### Implementation

The `BookListView` uses Django REST Framework's built-in backends to provide flexible querying:

- **Filtering:**  
  Enabled via `DjangoFilterBackend` and the `filterset_fields` attribute.  
  Users can filter books by `title`, `author`, and `publication_year`.

- **Searching:**  
  Enabled via `SearchFilter` and the `search_fields` attribute.  
  Users can search for books by `title` or the related author's `name`.

- **Ordering:**  
  Enabled via `OrderingFilter` and the `ordering_fields` attribute.  
  Users can order results by `title`, `publication_year`, or `author`.

#### View Configuration Example

```python
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year', 'author']
```

---

### Usage Examples

#### Filtering

- Get books published in 2025:
  ```
  GET /api/books/?publication_year=2025
  ```
- Get books by a specific author (author ID = 3):
  ```
  GET /api/books/?author=3
  ```
- Get books with a specific title:
  ```
  GET /api/books/?title=MyBookTitle
  ```

#### Searching

- Search for books with "Harry" in the title or author name:
  ```
  GET /api/books/?search=Harry
  ```

#### Ordering

- Order books by title (ascending):
  ```
  GET /api/books/?ordering=title
  ```
- Order books by publication year (descending):
  ```
  GET /api/books/?ordering=-publication_year
  ```

---

### Summary

- **Filtering:** Use query parameters matching `filterset_fields`.
- **Searching:** Use the `search` query parameter.
- **Ordering:** Use the `ordering` query parameter with any field listed in `ordering_fields`.

These features make the API flexible and user-friendly for front-end and API consumers.