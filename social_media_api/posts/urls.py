from django.urls import path
from .views import PostListView, PostCreateView, PostUpdateView, PostDeleteView, PostDetailView, CommentCreateView, CommentDeleteView, CommentListView, CommentDetailView, CommentUpdateView

urlpatterns = [
    path('api/', PostListView.as_view(), name='post-list'),
    path('api/create/', PostCreateView.as_view(), name='post-create'),
    path('api/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('api/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('api/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('api/<int:post_pk>/comments/', CommentListView.as_view(), name='comment-list'),
    path('api/<int:post_pk>/comments/create/', CommentCreateView.as_view(), name='comment-create'),
    path('api/<int:post_pk>/comments/<int:comment_pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('api/<int:post_pk>/comments/<int:comment_pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
    path('api/<int:post_pk>/comments/<int:comment_pk>/', CommentDetailView.as_view(), name='comment-detail'),
]