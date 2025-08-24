from .serializers import PostSerializer, CommentSerializer
from django.contrib.auth import get_user_model 
from django.db.models import Q
from .models import Post, Comment
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly


User = get_user_model()

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.query_params.get('search')
        author = self.request.query_params.get('author')
        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) | Q(content__icontains=search)
            )
        if author:
            queryset = queryset.filter(author__username=author)
        return queryset

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = super().get_queryset()
        post_pk = self.request.query_params.get('post_pk')
        search = self.request.query_params.get('search')
        author = self.request.query_params.get('author')
        if post_pk:
            queryset = queryset.filter(post_id=post_pk)
        if search:
            queryset = queryset.filter(content__icontains=search)
        if author:
            queryset = queryset.filter(author__username=author)
        return queryset


class UserFollowingFeedViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    ordering = ['-created_at']

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            following_users = user.following.all()
            return Post.objects.filter(author__in=following_users).order_by('-created_at')
        return Post.objects.none()