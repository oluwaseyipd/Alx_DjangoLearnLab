from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from .serializers import UserSerializer, RegisterSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

# User Registration
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


# User Login and Token Retrieval
class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)

        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key, "user": UserSerializer(user).data})
        return Response({"error": "Invalid Credentials"}, status=400)


# Example Protected Route (to test tokens)
class ProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

class FollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, username):
        try:
            user_to_follow = User.objects.get(username=username)
            if user_to_follow == request.user:
                return Response({"error": "You cannot follow yourself."}, status=400)
            request.user.following.add(user_to_follow)
            return Response({"status": f"You are now following {username}."})
        except User.DoesNotExist:
            return Response({"error": "User not found."}, status=404)

class UnFollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, username):
        try:
            user_to_unfollow = User.objects.get(username=username)
            if user_to_unfollow == request.user:
                return Response({"error": "You cannot unfollow yourself."}, status=400)
            request.user.following.remove(user_to_unfollow)
            return Response({"status": f"You have unfollowed {username}."})
        except User.DoesNotExist:
            return Response({"error": "User not found."}, status=404)