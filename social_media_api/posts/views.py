from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from .serializers import PostSerializer, CommentSerializer
from django.contrib.auth import get_user_model 
from django.db.models import Q
from .models import Post, Comment
from rest_framework.permissions import IsAuthenticated, AllowAny


User = get_user_model()


class PostListView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        queryset = Post.objects.all()
        search = request.query_params.get('search')
        author = request.query_params.get('author')
        
        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) | Q(content__icontains=search)
            )
        if author:
            queryset = queryset.filter(author__username=author)
        
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

class PostCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class PostUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    def put(self, request, pk):
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

class PostDeleteView(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response(status=204)

class PostDetailView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

class CommentListView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, post_pk):
        post = Post.objects.get(pk=post_pk)
        comments = post.comments.all()
        search = request.query_params.get('search')
        author = request.query_params.get('author')

        if search:
            comments = comments.filter(content__icontains=search)
        if author:
            comments = comments.filter(author__username=author)

        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

class CommentCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, post_pk):
        post = Post.objects.get(pk=post_pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(post=post)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class CommentUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    def put(self, request, post_pk, comment_pk):
        post = Post.objects.get(pk=post_pk)
        comment = post.comments.get(pk=comment_pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class CommentDeleteView(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request, post_pk, comment_pk):
        post = Post.objects.get(pk=post_pk)
        comment = post.comments.get(pk=comment_pk)
        comment.delete()
        return Response(status=204)



class CommentDetailView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, post_pk, comment_pk):
        post = Post.objects.get(pk=post_pk)
        comment = post.comments.get(pk=comment_pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
