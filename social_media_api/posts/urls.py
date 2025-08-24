from django.urls import path
from .views import PostListView, PostCreateView, PostUpdateView, PostDeleteView, PostDetailView, CommentCreateView, CommentDeleteView, CommentListView, CommentDetailView, CommentUpdateView

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/create/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:post_pk>/comments/', CommentListView.as_view(), name='comment-list'),
    path('posts/<int:post_pk>/comments/create/', CommentCreateView.as_view(), name='comment-create'),
    path('posts/<int:post_pk>/comments/<int:comment_pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('posts/<int:post_pk>/comments/<int:comment_pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
    path('posts/<int:post_pk>/comments/<int:comment_pk>/', CommentDetailView.as_view(), name='comment-detail'),
]