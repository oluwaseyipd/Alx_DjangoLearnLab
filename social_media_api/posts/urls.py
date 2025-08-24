from django.urls import path
from .views import PostViewSet, CommentViewSet, UserFollowingFeedViewSet

urlpatterns = [
    path('posts/', PostViewSet.as_view({'get': 'list', 'post': 'create'}), name='post-list'),
    path('posts/<int:pk>/', PostViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='post-detail'),
    path('posts/<int:post_pk>/comments/', CommentViewSet.as_view({'get': 'list', 'post': 'create'}), name='comment-list'),
    path('posts/<int:post_pk>/comments/<int:pk>/', CommentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='comment-detail'),
    path('feed/', UserFollowingFeedViewSet.as_view({'get': 'list'}), name='user-following-feed'),
]