from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
    IsAuthenticatedOrReadOnly,
    IsAdminUser
)

from post.models import Post
from post.serializers import PostSerializer
from post.permissions import MyIsAuthenticated, IsOwner,IsDiyoraPermission, IsAdmin


# Create your views here.

class PostListView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [MyIsAuthenticated]


class PostDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsDiyoraPermission]
    lookup_field = 'pk'

class OnlyAdmin(RetrieveUpdateDestroyAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    permission_classes=[IsAdmin]
    lookup_field = 'pk'