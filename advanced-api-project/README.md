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